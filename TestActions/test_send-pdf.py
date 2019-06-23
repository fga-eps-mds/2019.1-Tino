import requests

url = 'https://2f23418f.ngrok.io'


def test_send_pdf():

    requestConn = requests.get(url)
    assert requestConn.status_code == 200
