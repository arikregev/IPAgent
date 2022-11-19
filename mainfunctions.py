import pip._vendor.requests as requests
import tempfile
import json
from exceptions import handleException

GLOBAL_EXIT_CODE : int = 0

def queryMyIP():
    try:
        response = requests.get("http://ifconfig.me")
        return response.text
    except Exception as e:
        handleException(message = "Unable to get current ip address", exception = e, exitCode = 2)

def openCacheFile(fileName: str):
    try:
        filepath = tempfile.gettempdir() + '/' + fileName
        return open(filepath, 'r')
    except FileNotFoundError as e:
        #call create File
        return createCacheFile(filepath)

def createCacheFile(filepath: str):

    try:
        return open(filepath, 'x')
    except Exception as e:
        handleException("unable to create Temp File", e)
        #If cache can't be created terminate? or continue without cahce and validate with cloud?

def readJsonFile(file):
    try:
        return json.loads(file)
    except Exception as e:
        print(e)
        #If cache can't be read terminate? or continue without cahce and validate with cloud?


def writeIPtoJsonFile(ip: str):
    try:
        json.dump({"ip": ip})
    except Exception as e:
        print(e)