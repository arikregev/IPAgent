from enum import Enum
class ExitCode(Enum):
    """
    Enum for exit codes

    Args:
        SUCCESS_NO_CHANGE (0): No change was made, the IP address in cache matched for latest query.
        SUCCESS_W_CHANGE (1): Change was made, either current ip was different then the address in cache,
            or cache wasn't available and was updated. either way a cloud update was initiated.
        GENERAL_ERROR (2): An Error that was not defined yet detected
    """
    SUCCESS_NO_CHANGE = 0
    SUCCESS_W_CHANGE = 1
    GENERAL_ERROR = 2
    UNABLE_TO_GET_CURRENT_IP = 3

def initGlobalExitCode():
    exitCode = ExitCode.SUCCESS_NO_CHANGE