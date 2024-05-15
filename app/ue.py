from app.general import sendRequest
from constants import UEInfoURL, setNewUEURL


def getUEInfo(imsi):
    return sendRequest(UEInfoURL(imsi))


def setNewUE(imsi, n: int = 0):
    return sendRequest(setNewUEURL(imsi, n))
