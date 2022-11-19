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
        #If cache can't be read terminate? or continue without cahce and validate with cloud?
    finally:
        jsonFile.close()

def checkIPinJson(json: dict, currentIP):
    if(json == None or json['ip'] != currentIP):
        raise ChangeCacheException()

