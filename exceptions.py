"""
A file for exception related classes
"""
from exitcode import ExitCode
class GeneralException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ChangeException(GeneralException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ChangeCacheException(ChangeException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UpdateCloudException(ChangeException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UpdateCacheAndCloudException(UpdateCloudException, ChangeCacheException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UnableToGetCurrentIPException(GeneralException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)