from constants import plmnID


def getFromatedIMSI(number):
    base = '0' * 10
    return f'imsi-{plmnID}{base[:10 - len(str(number))] + str(number)}'

