import sys
import simplejson as json
from bs4 import BeautifulSoup


POS_TABLE = {
    'Noun': 'n',
    'Verb': 'v',
    'Particle': 'part',
    'Adjective': 'a',
    'Adverb': 'adv',
    'Determiner': 'det',
    'Proper noun': 'propn',
    'Pronoun': 'pron',
    'Interjection': 'intj',
    'Abbreviation': 'abbrev',
    'Suffix': 'suf',
    'Numeral': 'num',
    'Prefix': 'pref',
}

def clean_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.text
    text = text.replace('"', '\\"')

    return '"{}"'.format(text)


def main():
    all_data = []
    for line in sys.stdin:
        data = json.loads(line)
        all_data.append(data)

    all_data.sort(key=lambda data: data['word'])

    for data in all_data:
        word = data['word']
        senses = data['definition'].get('ko')
        if not senses:
            continue
        for sense in senses:
            if sense['partOfSpeech'] in {'Symbol', 'Syllable', 'Phrase', 'Proverb'}:
                continue
            print('- word: {}'.format(word))
            if 'pron' in data:
                print('  romaja: {}'.format(data['pron']))

            pos = POS_TABLE[sense['partOfSpeech']]
            print('  pos: {}'.format(pos))

            print('  defs:')
            for definition in sense['definitions']:
                print('    - def: {}'.format(clean_html(definition['definition'])))

                examples = definition.get('parsedExamples')
                if examples:
                    print('      examples: ')
                    for example in examples:
                        print('        - example: {}'.format(clean_html(example['example'])))
                        if 'transliteration' in example:
                            print('          transliteration: {}'.format(clean_html(example['transliteration'])))
                        if 'translation' in example:
                            if '\n' in example['translation']:
                                xlitr, xlat = example['translation'].split('\n')
                                print('          transliteration: {}'.format(clean_html(xlitr)))
                                print('          translation: {}'.format(clean_html(xlat)))
                            else:
                                print('          translation: {}'.format(clean_html(example['translation'])))
            if 'conj' in data:
                conj_str = ', '.join(conj.replace(', ', '/') for conj in data['conj'])
                print('  conj: [{}]'.format(conj_str))
            print('')


if __name__ == '__main__':
    main()
