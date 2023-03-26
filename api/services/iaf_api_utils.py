# Python
import requests
from datetime import datetime
import phonenumbers


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
    """ Https request to get the list of appointment in the date

    Args:
        date (date): the date of list appointment
        token (str): token authentication

    Returns:
        json: Appointment list in json format.
    """

    url = f"https://api-iaf.alexanderfleming.org/apigeosalud/api/v1/os/byTipoFchEstid/1056/{date}/2"
    headers = {"x-access-token": token}
    response = requests.get(url, headers=headers)

    return response.json()["data"]

def get_pacient_data(person_id, token):
    """Get the patient contact information 

    Args:
        person_id (int): person_id
        token (str): token authentication

    Returns:
        json: patient contact information
    """
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
    """Preproces the appointment data to keep only the
    necesary information

    Args:
        appoinment_list (json): appoinment_list

    Returns:
        list: the data clean and selected
    """
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

def normalize_number(raw_number):
    """Normalized number

    Args:
        raw_number (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    # Remover el sufijo '15' si está presente
    if raw_number.startswith('15') and len(raw_number) == 10:
        raw_number = '911' + raw_number[2:]
    elif raw_number.startswith('11') and len(raw_number) == 10:
        raw_number = '911' + raw_number[2:]
    elif raw_number.startswith('5491115') and '15' in raw_number:
        raw_number = raw_number.replace('15', '', 1)
    elif raw_number.startswith('54015') and '15' in raw_number:
        raw_number = raw_number.replace('15', '11', 1)

    try:
        # Analizar el número de teléfono
        parsed_number = phonenumbers.parse(raw_number, "AR")

        # Verificar si el número es válido
        if not phonenumbers.is_valid_number(parsed_number):
            print(f"El número de teléfono {raw_number} no es válido, se reemplazo por el de Brenda")
            parsed_number = 5491135723096
            return parsed_number
            # raise ValueError(f"El número de teléfono {raw_number} no es válido.")

        # Formatear el número al formato E.164
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

        return formatted_number[1:]
    except phonenumbers.NumberParseException:
        raise ValueError(f"No se pudo analizar el número de teléfono {raw_number}")
 

def preproces_patient_contact_info(patient_info):
    """Preproces the contact patient information to 
    keep only the necesary information


    Args:
        patient_info (json): Dict or json with the information to
        preproces

    Returns:
        list: information cleaned
    """

    patient_info = [
        {
            k: int(v) if k == 'persCelular' and v else v 
            for k, v in d.items() if k in ['idpersona', 'persCelular', 'persmail']
        } if d.get('persCelular', None) else 
        {
            'idpersona': d.get('idpersona', None),
            'persCelular': d.get('telefono', None),
            'persmail': d.get('persmail', None)
        }
        for d in patient_info
    ]
    # # Normalize the number
    # raw_number = patient_info[0]["persCelular"]
    # normalized_number = normalize_number(str(raw_number))
    # patient_info[0]["persCelular"] = int(normalized_number)

    return patient_info[0]
