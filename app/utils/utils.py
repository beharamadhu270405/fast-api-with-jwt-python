import requests


def verify_password(username, password):
    if username == 'admin' and password == 'admin':
        return True
    return False


def get_usa_population_yearwise():
    url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population"
    response = requests.request("GET", url)
    return response.json()
