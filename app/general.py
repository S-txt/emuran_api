import requests

from app.ue import getSubscibedUE, setNewSubscriber, getFromatedIMSI
from constants import header, UEInfoURL, setNewUEURL
from ue_config import getSubsscriberSettings


def sendRequest(url, payload=None, method='GET'):
    """ Make request from params and handle response """
    match method:
        case 'GET':
            response = requests.get(url, headers=header)
        case 'POST':
            response = requests.post(url, headers=header, json=payload)

    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception(f'Got error {response.status_code} due request: "{url}"')

def setUE(n, offset=len(getSubscibedUE()) + 2):
    """ registrate and create N of UE's"""

    print(f'Subscribers: {len(getSubscibedUE())}')
    print(f'Set profiles...')

    for id in range(1, n + 1):
        setNewSubscriber(getSubsscriberSettings(getFromatedIMSI(id + offset)))
    new_subs = getSubscibedUE()

    print(f'\nUpdates or creates subscribers: {len(new_subs)}')
    print('Profiles info:')
    for sub in new_subs:
        print(sub)

    print("\nCreating UE's:")
    setNewUE(getFromatedIMSI(offset + 1), n)
