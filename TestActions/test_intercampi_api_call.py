import requests
import json

# specify which host you're going to use (production or local)
url = 'https://8a8e50e8.ngrok.io'
url_darcy = url + "/darcy"
url_gama = url + "/gama"
url_planaltina = url + "/planaltina"
url_ceilandia = url + "/ceilandia"


def test_all_path():

    request = requests.get(url)
    assert request.status_code == 200


def test_gama_path():

    request = requests.get(url_gama).json()
    requestConn = requests.get(url_gama)
    json_data = request
    assert requestConn.status_code == 200
    assert json_data[0]['origem'] == 'Gama'  # asserts data is comming


def test_planaltina_path():

    request = requests.get(url_planaltina).json()
    requestConn = requests.get(url_planaltina)
    json_data = request
    assert requestConn.status_code == 200
    assert json_data[0]['origem'] == 'Planaltina'


def test_ceilandia_path():

    request = requests.get(url_ceilandia).json()
    requestConn = requests.get(url_ceilandia)
    json_data = request
    assert requestConn.status_code == 200
    assert json_data[0]['origem'] == 'Ceilândia'


def test_darcy_path():

    request = requests.get(url_darcy).json()
    requestConn = requests.get(url_darcy)
    json_data = request
    assert requestConn.status_code == 200
    assert json_data[0]['origem'] == 'Darcy Ribeiro'
