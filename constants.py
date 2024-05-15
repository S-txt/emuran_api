token = 'admin'
header = {
    "Token": f'{token}'
}

# external ip address of free5GC server
base_url = 'http://<ip>:5000/api'

# external ip adress of UERANSIM server
ueransim_api_url = 'http://<ip>'


plmnID = '20893'

subscruberURL = f'{base_url}/subscriber/'

def UEInfoURL(imsi: str): return f'{ueransim_api_url}/ue/info/{imsi}'


def setNewUEURL(imsi: str, n: int = 0): return f'{ueransim_api_url}/ue/set/{imsi}?n={n}'
