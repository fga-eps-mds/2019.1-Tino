import requests

url = 'https://cf304252.ngrok.io'

def test_send_pdf():

    request = requests.get(url)
    requestConn = requests.get(url)
    assert requestConn.status_code == 200