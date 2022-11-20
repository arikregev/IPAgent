import pip._vendor.requests as requests 
import json
from exceptions import UnableToGetCurrentIPException

def queryMyIP():
    """
    A function the returns the current IP Address of the client computer.
    Returns:
        str: current IP Address of the client computer.
    """
    try:
        return requests.get("http://ifconfig.me").text
    except Exception:
        raise UnableToGetCurrentIPException()

def writeIPtoJsonFile(filePath: str, ip: str):
    """A function for writing to the json cache file.
    Args:
        filePath (str): path to cache file string.
        ip (str): urrent IP Address of the client computer.
    """
    try:
        with open(filePath, 'w') as jsonFile:
            json.dump({"ip": ip}, jsonFile)
    except Exception as e:
        print(e) #TODO
    finally:
        jsonFile.close()