# Python
import requests
from datetime import datetime


# env
from config.config import iafsettings 

def authentication():
    """
    Authentication for the IAF API

    Returns:
        str: token authentication
    """
    # Set login info from config file base on pydantic BaseSetting model
    url = iafsettings.IAF_API_URL_LOGIN
    headers = iafsettings.HEADERS
    username = iafsettings.IAF_USERNAME
    password = iafsettings.IAF_PASSWORD

    # Post request
    response = requests.get(url, headers=headers, auth=(username, password))

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
        token (str): acces token

    Returns:
        str: token authentication
    """

    # Set login info from config file base on pydantic BaseSetting model
    url = iafsettings.IAF_API_URL_RE_LOGIN
    headers = {"x-access-token": f"{token}"}

    # Post request
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Login successful
        print("Login successful")

        if "token" in response.json():
            return response.json()["token"]
    else:
        # Login failed
        return response.status_code
        

def get_appointment_list(date, token):

    url = f"https://api-iaf.alexanderfleming.org/apigeosalud/api/v1/os/byTipoFchEstid/1056/{date}/2"
    headers = {"x-access-token": token}
    response = requests.get(url, headers=headers)

    return response.json()["data"]

def get_pacient_data(person_id, token):
    url = f"https://api-iaf.alexanderfleming.org/apigeosalud/api/v1/patient/bypersid/{person_id}"
    headers = {"x-access-token": token}
    response = requests.get(url, headers=headers)

    return response.json()["data"]

def get_practice(OsId, token):
    url = f"https://api-iaf.alexanderfleming.org/apigeosalud/api/v1/osindicact/byosid/1056/1972{OsId}"
    headers = {"x-access-token": token}
    response = requests.get(url, headers=headers)

    return response.json()["data"]

def preproces_appoinment_data(appoinment_list):
    processed_list = []

    for item in appoinment_list:
        full_name = item['nombre'].strip()
        if item['nombre1']:
            full_name += ' ' + item['nombre1'].strip()
        
        full_last_name = item['apellido'].strip()
        if item['apellido1']:
            full_last_name += ' ' + item['apellido1'].strip()

        date_parts = item['fecha'].split()
        date_only = date_parts[0]
        time_only = date_parts[1]
        
        processed_list.append({
            'idpersona': item['idpersona'],
            'OsId': item['OsId'],
            'date_only': date_only,
            'time_only': time_only,
            'last_name': full_last_name,
            'first_name': full_name,
            'rrhhid': item['rrhhid']
        })
    
    return processed_list