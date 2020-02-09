import requests

def readme():
    test_url = "https://raw.githubusercontent.com/JohnLockwood/sam-python-with-layers/master/tests/LayerSampleText.txt"
    resp = requests.get(test_url)
    if resp.status_code == requests.status_codes.codes.OK :
        return resp.text
    else:
        return "Unable to get README content, status received: " + str(resp.status_code)

