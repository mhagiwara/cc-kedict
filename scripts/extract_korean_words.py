import sys
import re
import unicodedata

def main():
    for line in sys.stdin:
        match = re.search('<title>(.*)</title>', line)
        if match:
            word = match.group(1)
            if all(unicodedata.name(c).startswith('HANGUL SYLLABLE') for c in word):
                print(word)


if __name__ == '__main__':
    main()
