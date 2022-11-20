from exitcode import ExitCode

class ChangeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        global exitCode
        exitCode = ExitCode.SUCCESS_W_CHANGE

class ChangeCacheException(ChangeException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UpdateCloudException(ChangeException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class UpdateCacheAndCloudException(UpdateCloudException, ChangeCacheException):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)