from app.general import sendRequest
from constants import subscruberURL


def getSubscibedUE():
    return sendRequest(subscruberURL)


def getSubscriberInfo(ueId, plmnID):
    return sendRequest(f'{subscruberURL}{ueId}/{plmnID}')


def setNewSubscriber(data):
    return sendRequest(f'{subscruberURL}{data["ueId"]}/{data["plmnID"]}', data, 'POST')

