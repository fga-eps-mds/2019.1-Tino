import requests

url = 'https://1326be41.ngrok.io'

def test_send_pdf():

    request = requests.get(url)
    requestConn = requests.get(url)
    assert requestConn.status_code == 200