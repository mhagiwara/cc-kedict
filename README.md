# cc-kedict: Creative Commons Korean-English Dictionary 

[![CircleCI](https://circleci.com/gh/mhagiwara/cc-kedict.svg?style=svg)](https://circleci.com/gh/mhagiwara/cc-kedict)

This dictionary is available under the [Creative Commons Attribution-ShareAlike (CC BY-SA 3.0) License](https://creativecommons.org/licenses/by-sa/3.0/).

Currently most of the dictionary data is based on [English Wiktionary](https://en.wiktionary.org/), but our plan is to improve it in terms of both coverage and content. Let me know if you are interested in contributing!

## Data structure

The main dictionary file is [kedict.yml](kedict.yml). It is written in YAML, which is a friendly format both for humans and computers.

The entire dictionary is a huge list of associative arrays, where each array represents one entry of the dictionary. Each array has the following keys:

- `word` (mandatory): the word surface form
- `pos` (mandatory): part of speech. See [pos.yml](pos.yml) for the definition
- `defs` (mandatory): list of definitions. Each definition contains `def` and `examples` fields.
- `romaja` (optional): romanized form of the word. We use [The Revised Romanization of Korean](https://en.wikipedia.org/wiki/Revised_Romanization_of_Korean) as the romanization system.
- `hanja` (optional): hanja (Chinese character) form of the word, if any
- `conj` (optional): conjugation table. Currently, this is a four-element array that contains formal non-polite, informal non-polite, informal polite, and formal polite forms.
- `notes` (optional): grammar and usage notes
- `tags` (optional): list of tags assigned to the entry
- `syns` (optionsl): synonyms
- `ants` (optional): antonyms
- `rels` (optional): related words
- `cf` (optional): "see also" words
- `ders` (optional): derived terms

[validate.py](validate.py) is a Python script that validates the format of `kedict.yml`, which requires `PyYAML` package to run.  It shows `Validation: PASSED` if it succeeds in validatating the file.
