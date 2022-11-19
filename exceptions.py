from typing import overload

@overload
def handleException(message: str, e: Exception):
    print(f"Exception thrown: {message}\n{e}")

@overload
def handleException(message: str, exception: Exception, exitCode: int):
    handleException(message, exception)
    GLOBAL_EXIT_CODE = exitCode