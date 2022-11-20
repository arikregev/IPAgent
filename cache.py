import os, json
from exceptions import ChangeCacheException

def checkCacheFile(filePath: str):
    if not os.path.exists(filePath):
        raise ChangeCacheException()

def readJsonFile(filePath):
    try:
        with open(filePath, 'r') as jsonFile:
            return json.load(jsonFile)
    except:
        raise ChangeCacheException()
    finally:
        jsonFile.close()

def checkIPinJson(json: dict, currentIP):
    if(json == None or json['ip'] != currentIP):
        raise ChangeCacheException()

