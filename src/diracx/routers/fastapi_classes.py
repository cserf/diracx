from __future__ import annotations

import asyncio
import contextlib
import inspect
from functools import partial

from fastapi import APIRouter, FastAPI
from pydantic import BaseSettings

from diracx.db.utils import BaseDB

# Rules:
# All routes must have tags (needed for auto gen of client)
# Form headers must have a description (autogen)
# methods name should follow the generate_unique_id_function pattern


class DiracFastAPI(FastAPI):
    def __init__(self):
        @contextlib.asynccontextmanager
        async def lifespan(app: DiracFastAPI):
            async with contextlib.AsyncExitStack() as stack:
                await asyncio.gather(
                    *(stack.enter_async_context(f()) for f in app.lifetime_functions)
                )
                yield

        self.lifetime_functions = []
        super().__init__(
            swagger_ui_init_oauth={
                "clientId": "myDIRACClientID",
                "scopes": "property:NormalUser",
                "usePkceWithAuthorizationCodeGrant": True,
            },
            generate_unique_id_function=lambda route: f"{route.tags[0]}_{route.name}",
            title="Dirac",
            lifespan=lifespan,
        )

    def openapi(self, *args, **kwargs):
        if not self.openapi_schema:
            super().openapi(*args, **kwargs)
            for _, method_item in self.openapi_schema.get("paths").items():
                for _, param in method_item.items():
                    responses = param.get("responses")
                    # remove 422 response, also can remove other status code
                    if "422" in responses:
                        del responses["422"]
        return self.openapi_schema

    def include_router(self, router: APIRouter, *args, settings=None, **kwargs):
        super().include_router(router, *args, **kwargs)
        # If the router is a DiracRouter
        if not isinstance(router, DiracRouter):
            assert settings is None
            return

        assert router.prefix

        assert settings is not None
        self.dependency_overrides[settings.create] = lambda: settings
        for db in settings.databases:
            assert db.__class__ not in self.dependency_overrides
            self.lifetime_functions.append(db.engine_context)
            self.dependency_overrides[db.__class__] = partial(lambda xxx: xxx, db)


class ServiceSettingsBase(BaseSettings, allow_mutation=False):
    @classmethod
    def create(cls):
        return cls()

    @property
    def databases(self):
        annotations = inspect.get_annotations(self.__class__, eval_str=True)
        for field, metadata in annotations.items():
            for type_ in getattr(metadata, "__metadata__", tuple()):
                if issubclass(type_, BaseDB):
                    yield type_(getattr(self, field))


class DiracRouter(APIRouter):
    _registry: dict[type[ServiceSettingsBase], DiracRouter] = {}

    def __init__(
        self,
        *,
        tags,
        dependencies=None,
        settings_class: type[ServiceSettingsBase],
        prefix: str,
    ):
        super().__init__(tags=tags, dependencies=dependencies)
        assert settings_class not in self._registry
        self._registry[settings_class] = self
        self.prefix = prefix
