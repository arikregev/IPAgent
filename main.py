from mainfunctions import queryMyIP, writeIPtoJsonFile
from exceptions import ChangeCacheException, UpdateCloudException
import tempfile, os
from cache import checkCacheFile, readJsonFile, checkIPinJson
from exitcode import ExitCode


def main():
    try:
        exitCode: ExitCode = ExitCode.SUCCESS_NO_CHANGE
        filepath = tempfile.gettempdir() + '/' + 'IPAgent.json'
        current = queryMyIP() #Step 1: query my current IP address.
        
        #Step 2: check aginst local cache.
        checkCacheFile(filepath) #if file isn't exist ChangeCacheException will be thrown.
        json = readJsonFile(filepath) #If file isn't readable ChangeCacheException will be thrown.
        checkIPinJson(json, current) #If JSON is empty or IP address won't match ChangeCacheException will be thrown.
        
        #Step 3: TODO: check cloud and Update.

    except ChangeCacheException as e: #update cache process
        writeIPtoJsonFile(filepath, current)
        exitCode = ExitCode.SUCCESS_W_CHANGE
    except UpdateCloudException:
        #TODO: Update Cloud
        print()
        exitCode = ExitCode.SUCCESS_W_CHANGE
    except Exception as e:
        print(e)
        exitCode = ExitCode.GENERAL_ERROR

    finally:
        os._exit(exitCode.value)

if __name__ == "__main__":
    main()