import ssl
import pandas as pd
import json
from urllib import request as rq


def get_ssl_certificate():

    url = "https://fga.unb.br/guia-fga/horario-dos-onibus-intercampi"
    context = ssl._create_unverified_context()
    response = rq.urlopen(url, context=context)
    html = response.read()

    return html


def test_get_from_fga_site():

    html = get_ssl_certificate()
    tables = pd.read_html(html, header=0)
    first_table = tables[0]
    # convert to dataframe
    first_table = pd.DataFrame(first_table)
    first_table = first_table.to_json(orient='values')
    # convert string to json
    first_table = json.loads(first_table)
    result = []

    for item in first_table:
        element = {}
        element = {'horario_saida': item[0], 'destino': item[2],
                   'origem': item[1]}
        result.append(element)

    first = ""
    for each in result:
        first = each['destino']
        break

    assert first == 'Darcy Ribeiro'
