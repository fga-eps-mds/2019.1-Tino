import requests
import json
from urllib import request as rq
import os

url ='https://4f61d63e.ngrok.io'    #os.environ.get('INTERCAMPI_WEBHOOK')
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
    json = request  
    assert requestConn.status_code == 200
    assert json[0]['origem'] == 'Gama'
    

def test_planaltina_path():

    request = requests.get(url_planaltina).json()
    requestConn = requests.get(url_planaltina)
    json = request  
    assert requestConn.status_code == 200
    assert json[0]['origem'] == 'Planaltina'

def test_ceilandia_path():

    request = requests.get(url_ceilandia).json()
    requestConn = requests.get(url_ceilandia)
    json = request  
    assert requestConn.status_code == 200
    assert json[0]['origem'] == 'Ceilândia'

def test_darcy_path():

    request = requests.get(url_darcy).json()
    requestConn = requests.get(url_darcy)
    json = request  
    assert requestConn.status_code == 200
    assert json[0]['origem'] == 'Darcy Ribeiro'            