import sys
import re
import unicodedata
import simplejson as json

def is_korean_word(word):
    for c in word:
        try:
            if not unicodedata.name(c).startswith('HANGUL SYLLABLE'):
                return False
        except ValueError:
            return False
    return True


def main():
    for line in sys.stdin:
        match = re.search('<title>(.*)</title>', line)
        if match:
            word = match.group(1)
            if is_korean_word(word):
                print(json.dumps({'word': word}, ensure_ascii=False))


if __name__ == '__main__':
    main()
