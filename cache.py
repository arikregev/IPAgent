import os, json
from exceptions import ChangeCacheException

def checkCacheFile(filePath: str):
    """
    A function for verifying there is cache file.
    Args:
        filePath (str): path to cache file string.

    Raises:
        ChangeCacheException: an exception for initiating writing to cache.
    """
    if not os.path.exists(filePath):
        raise ChangeCacheException()

def readJsonFile(filePath: str):
    """
    A function to read cache file (data) after verifying that file exists.
    Args:
        filePath (str): path to cache file string.

    Raises:
        ChangeCacheException: an exception for initiating writing to cache.

    Returns:
        dict: json content
    """
    try:
        with open(filePath, 'r') as jsonFile:
            return json.load(jsonFile)
    except:
        raise ChangeCacheException()
    finally:
        jsonFile.close()

def checkIPinJson(json: dict, currentIP):
    """
    A function for checking cache (json) content and compare it with current ip address.

    Args:
        json (dict): content of cache file converted to json.
        currentIP (str): current ip address of machine running this client.

    Raises:
        ChangeCacheException: an exception for initiating writing to cache.
    """
    if(json == None or json['ip'] != currentIP):
        raise ChangeCacheException()

