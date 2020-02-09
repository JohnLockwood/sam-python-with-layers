import requests

def readme():
    resp = requests.get("https://raw.githubusercontent.com/JohnLockwood/getting-started-with-poetry/master/poetry-lambda-layer/README.rst")    
    if resp.status_code == requests.status_codes.codes.OK :
        return resp.text
    else:
        return "Unable to get README content, status received: " + str(resp.status_code)

