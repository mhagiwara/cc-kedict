import sys
import time

import requests
import simplejson as json
from bs4 import BeautifulSoup


def get_pron_conj(word):
    r = requests.get('https://en.wiktionary.org/api/rest_v1/page/html/{}'.format(word))
    soup = BeautifulSoup(r.text, 'html.parser')
    elements = soup.find_all('td', class_='IPA')

    if elements:
        pron = elements[0].text
    else:
        pron = None

    table = soup.find('table', class_='inflection-table')

    conj = None
    if table:
        tds = table.find_all('tr')[2].find_all('td')
        conj = [td.find('span').text for td in tds]

    return (pron, conj)


def main():
    for line in sys.stdin:
        data = json.loads(line)
        word = data['word']
        print(word, file=sys.stderr)
        pron, conj = get_pron_conj(word)
        if pron:
            data['pron'] = pron
        if conj:
            data['conj'] = conj
        print(json.dumps(data, ensure_ascii=False))
        time.sleep(.1)


if __name__ == '__main__':
    main()
