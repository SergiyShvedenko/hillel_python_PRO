from faker import Faker
fake = Faker('en_US')

import requests


def generate_customers(lenght: int = 100) -> str:
    result = ''
    for i in range(lenght):
        result += fake.first_name() + ' --> ' + fake.ascii_email() + ';  '
    return result


def space_numbers():
    r = requests.get('http://api.open-notify.org/astros.json')
    number = str(r.json()["number"])
    return number
