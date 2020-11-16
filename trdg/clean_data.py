import unicodedata
import re


def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def normalize_twi(s):
    s = unicode_to_ascii(s)
    s = re.sub(r'([!.?])', r' \1', s)
    s = re.sub(r'[^a-zA-Z.,ƆɔɛƐ!?’\'\"\\\n]+', r'', s)
    s = re.sub(r'\s+', r' ', s)
    return s


def findall(s):
    x = re.findall('[ɔↃƆɔↄᴐᵋꜫɛƐꜪ]', s)
    return x


def main():
    with open('dicts/tw.txt') as f:
        data = f.readlines()
    return data
