import requests
import json
from urllib import request as rq

<<<<<<< HEAD
<<<<<<< HEAD
url ='https://5c50e905.ngrok.io'    #os.environ.get('INTERCAMPI_WEBHOOK')
=======
url ='https://4f759d37.ngrok.io'    #os.environ.get('INTERCAMPI_WEBHOOK')
>>>>>>> 1b907baf9d316e0a662c15ebf1b309fe7a818093
=======
url ='https://0dc0667e.ngrok.io'    #os.environ.get('INTERCAMPI_WEBHOOK')
>>>>>>> bc991322d5d21e3974938a2c4fec3ede74ba426e
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
