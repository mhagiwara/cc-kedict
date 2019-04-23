import yaml


MANDATORY_FIELDS = ['word', 'romaja', 'pos', 'senses']
OPTIONAL_FIELDS = ['index', 'hanja', 'conj', 'notes', 'tags', 'syns']
POS = ['n', 'v', 'a', 'pron', 'intj', 'det', 'part']
TAGS = ['topik1']


def validate_entry(entry):
    # TODO: Use JSON Schema instead to validate

    if not isinstance(entry, dict):
        raise ValueError('Entry {!r} is not a dict'.format(entry))

    for field in MANDATORY_FIELDS:
        if field not in entry:
            raise ValueError('Entry {!r} does not have the mandatory `{}` field'.format(entry, field))

    unrecognized_fields = set(entry.keys()) - set(MANDATORY_FIELDS) - set(OPTIONAL_FIELDS)
    if unrecognized_fields:
        raise ValueError('Entry {!r} has unrecognized field(s): {!r}'.format(entry, unrecognized_fields))

    if entry['pos'] not in POS:
        raise ValueError('Unrecognized POS tag: {}'.format(entry['pos']))

    if 'conj' in entry:
        if not isinstance(entry['conj'], list):
            raise ValueError('Conjugation {!r} is not a list'.format(entry['conj']))

    if 'tags' in entry:
        if not isinstance(entry['tags'], list):
            raise ValueError('Tags {!r} is not a list'.format(entry['tags']))
        for tag in entry['tags']:
            if tag not in TAGS:
                raise ValueError('Unrecognized tag: {}'.format(tag))


def validate_dictionary(data):

    if not isinstance(data, list):
        raise ValueError('The dictionary data is not a list')

    for entry in data:
        validate_entry(entry)

    for entry1, entry2 in zip(data, data[1:]):
        word1, word2 = entry1['word'], entry2['word']

        if not word1 <= word2:
            raise ValueError('word: {} and {} are not in an alphabetical order'.format(word1, word2))


def main():
    with open('kedict.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

        validate_dictionary(data)

        print('{} entries found.'.format(len(data)))
        print('Validation: PASSED')


if __name__ == '__main__':
    main()
