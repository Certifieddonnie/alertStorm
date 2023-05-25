# Validation Utils
from typing import Dict

def clean_data(data) -> Dict[str, str]:
    """ cleans up the request data """
    clean = {
        'email': data.get('email'),
        'password': data.get('password'),
        'city': data.get('city'),
        'country': data.get('country')
    }

    return clean
