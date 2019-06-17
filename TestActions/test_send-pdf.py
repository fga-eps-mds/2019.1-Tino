import requests

url = 'https://c8869937.ngrok.io'

def test_send_pdf():

    requestConn = requests.get(url)
    assert requestConn.status_code == 200