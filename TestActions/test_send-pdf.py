import requests

url = 'https://90ca1ab7.ngrok.io'


def test_send_pdf():

    requestConn = requests.get(url)
    assert requestConn.status_code == 200
