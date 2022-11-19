from exitcode import ExitCode
from mainfunctions import writeIPtoJsonFile

# @overload
# def handleException(message: str, e: Exception):
#     print(f"Exception thrown: {message}\n{e}")

# @overload
# def handleException(message: str, exception: Exception, exitCode: int):
#     handleException(message, exception)
#     GLOBAL_EXIT_CODE = exitCode

class ChangeException(Exception):
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