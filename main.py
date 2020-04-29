# -*- encoding: utf-8 -*-

import requests
import re
import json
import ast
import logging
import sys
import time
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%H:%M:%S', level=logging.INFO)

if __name__ == '__main__':

    # Recuperando a página do site
    try:
        logging.info('Recuperando a página do site com requests')
        response = requests.get('https://esaj.tjsp.jus.br/cpopg/open.do')
    except Exception as err:
        logging.error('ocorreu o erro %s ao acessar o site',err)
        logging.info('Fechando o App, verifique sua conexão internet!')
        sys.exit(1)
    else:
        logging.info('Recuperando o conteúdo da página : OK!')
        soup = BeautifulSoup(response.content, 'html.parser')

    # Isolando a função que contem o resultado esperado
    result = soup.find(string=re.compile("JSON.parse"))

    # Definindo o pattern da Regex a ser usada
    pattern = re.compile(r"\[(.+?)\]")

    # Isolando a linha que contem os dados para extrair a string
    aux = pattern.search(result)

    # Convertendo a string em list
    var = ast.literal_eval(aux.group(0))

    # Criando uma nova lista contendo só os nomes dos foros
    foros = [data['text'] for data in var if data['text'] != 'Todos os foros']

    # Convertendo a lista dos forros em json
    logging.info('Convertendo os dados em uma array json')
    foros = json.dumps(foros, indent=2, ensure_ascii=False)
    time.sleep(1)

    # E voilá
    print(foros)
    time.sleep(0.5)
    logging.info('Processo executado com sucesso!')