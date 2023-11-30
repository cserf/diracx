# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.10.1, generator: @autorest/python@6.4.11)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ChecksumAlgorithm(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enumeration."""

    SHA256 = "sha256"


class Enum0(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum0."""

    AUTHORIZATION_CODE = "authorization_code"


class Enum1(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum1."""

    URN_IETF_PARAMS_OAUTH_GRANT_TYPE_DEVICE_CODE = (
        "urn:ietf:params:oauth:grant-type:device_code"
    )


class Enum10(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum10."""

    ASC = "asc"


class Enum11(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum11."""

    DSC = "dsc"


class Enum2(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Enum2."""

    REFRESH_TOKEN = "refresh_token"


class Enum3(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Response Type."""

    CODE = "code"


class Enum4(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Code Challenge Method."""

    S256 = "S256"


class JobStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enumeration."""

    SUBMITTING = "Submitting"
    RECEIVED = "Received"
    CHECKING = "Checking"
    STAGING = "Staging"
    WAITING = "Waiting"
    MATCHED = "Matched"
    RUNNING = "Running"
    STALLED = "Stalled"
    COMPLETING = "Completing"
    DONE = "Done"
    COMPLETED = "Completed"
    FAILED = "Failed"
    DELETED = "Deleted"
    KILLED = "Killed"
    RESCHEDULED = "Rescheduled"


class SandboxFormat(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enumeration."""

    TAR_BZ2 = "tar.bz2"


class ScalarSearchOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enumeration."""

    EQ = "eq"
    NEQ = "neq"
    GT = "gt"
    LT = "lt"
    LIKE = "like"


class VectorSearchOperator(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """An enumeration."""

    IN = "in"
    NOT_IN = "not in"
