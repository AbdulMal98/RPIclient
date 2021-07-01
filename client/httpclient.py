import base64

import requests

user: str = "Mal"
password: str = "MGSgQYPRuI"


def postAtp(temperature, pressure, altitude, timestamp):
    datadict = {"timestamp": timestamp, "altitude": altitude, "temperature": temperature, "pressure": pressure}
    r = requests.post("https://sleepy-badlands-03259.herokuapp.com/add", json=datadict, headers=getBasicAuthHeader())
    print(r.status_code)


def getBasicAuthHeader():
    authVal = user + ":" + password
    authVal_bytes = authVal.encode('ascii')
    encodedVal = base64.b64encode(authVal_bytes)
    return {"Authorization": "Basic " + encodedVal.decode('ascii')}
