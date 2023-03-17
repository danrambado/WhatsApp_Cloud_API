# Python
import requests

# env
from config.config import IAFsettings #??????? check later 9/3 13hs

def authentication(url, headers, username, password):
    """
    Authentication for the IAF API

    Args:
        url (str): Login URL
        headers (str): headers
        username (str): username
        password (str): password

    Returns:
        str: token authentication
    """
    # Set login info
    url = url
    headers = headers
    username = username
    password = password

    # Post request
    response = requests.post(url, headers=headers, auth=(username, password))

    if response.status_code == 200:
        # Login successful
        print("Login successful")

        if "token" in response.json():
            return response.json()["token"]
    else:
        # Login failed
        return response.status_code
    
def re_authentication(token):
    """_summary_

    Args:
        token (_type_): _description_
    """
        

def get_appointment_list(date, token):

    url = f"http://10.10.10.97:8085/api/v1/os/byTipoFchEstid/1056/{date}/2"
    headers = {"x-access-token": token}
    response = requests.post(url, headers=headers)

    return response.json()["data"]


def procces_appointment_list():
    pass


def get_pacient_data():
    pass

def get_practice():
    pass
