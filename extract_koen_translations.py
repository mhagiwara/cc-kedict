import sys
import simplejson as json
import re
from bs4 import BeautifulSoup
import unicodedata


def format_subsection(subsection):
    """Convert a subsection (list of lines) to a clean string."""
    subsection_html = '\n'.join(subsection)
    subsection_html = subsection_html.replace('&lt;', '<').replace('&gt;', '>')
    soup = BeautifulSoup(subsection_html, 'html.parser')

    subsection_text = soup.text
    subsection_text = subsection_text.strip()

    return subsection_text


def is_valid_subsection_title(subsection_title):
    """Returns whether the given subsection title is a valid one"""
    if not subsection_title:
        return False
    if subsection_title in {'Hanja', 'Glyph origin', 'References', 'See also'}:
        return False
    return True


def extract_subsections(english_section):
    """Given a english section (list of lines), extract subsections as a dict"""
    subsection_title = ''
    subsection = []
    subsections = {}
    for line in english_section:
        if line.startswith('<h3>'):
            if subsection and is_valid_subsection_title(subsection_title):
                formatted_subsection = format_subsection(subsection)
                if formatted_subsection:
                    subsections[subsection_title] = formatted_subsection
                subsection = []
            m = re.match(r'<h3>(.*)</h3>', line)
            if m:
                subsection_title = m.group(1)
        else:
            subsection.append(line)

    if subsection and is_valid_subsection_title(subsection_title):
        formatted_subsection = format_subsection(subsection)
        if formatted_subsection:
            subsections[subsection_title] = formatted_subsection

    return subsections


def extract_translation(buffer):
    """Given a buffer (list of lines), extract English translation as a dict."""
    translation = {}
    in_korean_section = False
    korean_section = []
    for line in buffer:
        if line.startswith('<h1>'):
            m = re.match(r'<h1>(.*)</h1>', line)
            if m:
                translation['title'] = m.group(1)
        elif line.startswith('<h2>Korean</h2>'):
            in_korean_section = True
        elif line.startswith('<h2>'):
            in_korean_section = False
        elif in_korean_section:
            korean_section.append(line)

    if korean_section:
        subsections = extract_subsections(korean_section)
        if subsections:
            translation['korean'] = subsections
    return translation


def main():
    buffer = []
    for line in sys.stdin:
        if line.startswith('<doc '):
            # start of a document
            continue
        elif line.startswith('</doc>'):
            # enf of a document - extract translation and clear buffer
            translation = extract_translation(buffer)
            if 'korean' in translation:
                title = translation['title']
                if all(unicodedata.name(c).startswith('HANGUL SYLLABLE') for c in title):
                    print(json.dumps(translation, ensure_ascii=False))

            buffer = []
        else:
            buffer.append(line.strip())


if __name__ == '__main__':
    main()
