# cc-kedict: Creative Commons Korean-English Dictionary 

This dictionary is available under the [Creative Commons Attribution-ShareAlike (CC BY-SA 3.0) License](https://creativecommons.org/licenses/by-sa/3.0/).

The main dictionary file is [kedict.yml](kecit.yml). It is written in YAML, which is a friendly format both for humans and computers.

[validate.py](validate.py) is a Python script that validates the format of `kedict.yml`, which requires `PyYAML` package to run.  It shows `Validation: PASSED` if it succeeds in validatating the file.

Currently most of the dictionary data is based on [English Wiktionary](https://en.wiktionary.org/), but our plan is to improve it in terms of both coverage and content. Let me know if you are interested in contributing!
