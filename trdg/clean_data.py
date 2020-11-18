import unicodedata
import re


special_char1 = ['Ɔ', 'ɔ', 'ↄ', 'ᴐ', 'ɔ', 'ɔ', 'Ɔ', 'Ↄ', 'Ɔ', 'ɔ', 'ↄ', 'ᴐ', 'Ɔ']
special_char2 = ['ɛ', 'Ɛ', 'ɛ', 'Ɛ', 'ε', 'ɛ', 'Ɛ', 'ε']


'''Covert characters from unicode to ascii'''
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


'''Normalize special characters'''
def normalize(s):
    # s = unicode_to_ascii(s)
    s = re.sub(r'[^a-zA-ZƆɔɛƐↃƆɔↄᴐɛƐε’\'\"\n]+', r'', s)
    s = re.sub(r'\s+', r'', s)
    return s


'''Find all matches of words with special characters and clean them'''
def findall(s):
    print('----------------')
    print('STARTING')
    print('----------------')
    print(f'Length of data: {len(s)}')
    print('Normalizing words')
    s = [normalize(word) for word in s]
    match = []
    for idx, word in enumerate(s):
        for x in word:
            if x in set(special_char1+special_char2):
                match.append(s.pop(idx))
    print(f'Length of matched words: {len(match)}')
    clean = replace(match)
    print('----------------')
    print('Done')
    print('----------------')
    return s + clean


'''Cleaning'''
def replace(s):
    for i, word in enumerate(s):
        for idx, c in enumerate(word):
            if idx != 0:
                if c in set(special_char1):
                    t = list(word)
                    t[idx] = 'c'
                    s[i] = ''.join(t)
                if c in set(special_char2):
                    t = list(word)
                    t[idx] = special_char1[-1]
                    s[i] = ''.join(t)
    return s


def main():
    '''Open text file'''
    with open('tw.txt') as f:
        data = f.readlines()
    x = findall(data)

    '''Delete blank lines'''
    x = [line for line in x if line != '']

    '''Save cleaned text'''
    with open('tw1.txt', 'w') as f:
        f.write('\n'.join(x))


if __name__ == "__main__":
    main()
