"""Given a JSON-L file, this script scrapes the definition and adds it to each line."""

import sys
import time

import requests
import simplejson as json


def get_definition(word):
    r = requests.get('https://en.wiktionary.org/api/rest_v1/page/definition/{}'.format(word))
    return r.json()


def main():
    for line in sys.stdin:
        data = json.loads(line)
        word = data['word']
        data['definition'] = get_definition(word)
        print(json.dumps(data, ensure_ascii=False))
        print(word, file=sys.stderr)
        time.sleep(.1)


if __name__ == '__main__':
    main()
