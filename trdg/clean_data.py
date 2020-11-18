import unicodedata
import re


special_char1 = [chr(390), chr(596), chr(7440), chr(8579), chr(8580)] #Character codes for all occurances of"ɔ"
special_char2 = [chr(400), chr(603), chr(949)] #Character codes for all coccurance of "ɛ"
special_chars = special_char1 + special_char2

'''Covert characters from unicode to ascii'''
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


'''Normalize special characters'''
def normalize(s):
    s = unicode_to_ascii(s)
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
            if x in special_chars:
                match.append(s.pop(idx))
    print(f'Length of matched words: {len(match)}')
    clean = replace(match)
    print('----------------')
    print('Done')
    print('----------------')
    return s + clean


'''Cleaning'''
def replace(s):
    ords = []
    for i, word in enumerate(s):
        t = list(word)
        for idx, c in enumerate(t):
            if c in special_char1:
                tt = f'{ord(c)}'
                ords.append(tt)
                t[idx] = chr(99)
                print(t)
                s[i] = ''.join(t)
            if c in set(special_char2):
                t = list(word)
                t[idx] = special_char2[-1]
                s[i] = ''.join(t)

    with open('ords.txt', 'w') as f:
        f.write('\n'.join(ords))
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
