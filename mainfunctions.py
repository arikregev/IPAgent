import pip._vendor.requests as requests

def queryMyIP():
    try:
        response = requests.get("http://ifconfig.me")
        return response.text
    except:
        print(f"Exception thrown: unable to get current ip address")