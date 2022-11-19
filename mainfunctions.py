import pip._vendor.requests as requests 
import json

def queryMyIP():
    try:
        response = requests.get("http://ifconfig.me")
        return response.text
    except Exception as e:
        print(e)
        # handleException(message = "Unable to get current ip address", exception = e, 
        #     exitCode = ExitCode.UNABLE_TO_GET_CURRENT_IP)

def writeIPtoJsonFile(filePath, ip: str):
    try:
        with open(filePath, 'w') as jsonFile:
            json.dump({"ip": ip}, jsonFile)
    except Exception as e:
        print(e)
    finally:
        jsonFile.close()