from enum import Enum

class ExitCode(Enum):
    SUCCESS_NO_CHANGE = 0
    SUCCESS_W_CHANGE = 1
    GENERAL_ERROR = 2
    UNABLE_TO_GET_CURRENT_IP = 3