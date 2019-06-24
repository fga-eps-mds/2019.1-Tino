import requests

url = 'https://tinopro.com/pdf/'


def test_send_pdf():

    requestConn = requests.get(url)
    assert requestConn.status_code == 200
