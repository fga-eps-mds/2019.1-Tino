import requests

url = 'https://1e742be3.ngrok.io'#os.environ['INTERCAMPI_WEBHOOK']
url_darcy = url + "/darcy"
url_gama = url + "/gama"
url_planaltina = url + "/planaltina"
url_ceilandia = url + "/ceilandia"

def test_all_path():

    request = requests.get(url)

def test_gama_path():

    request = requests.get(url_gama)
    assert request.status_code == 200

def test_planaltina_path():

    request = requests.get(url_planaltina)
    assert request.status_code == 200

def test_ceilandia_path():

    request = requests.get(url_ceilandia)
    assert request.status_code == 200

def test_darcy_path():

    request = requests.get(url_darcy)
    assert request.status_code == 200            