import unicodedata
import re


'''Covert characters from unicode to ascii'''
def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


'''Normalize special characters'''
def normalize(s):
    s = unicode_to_ascii(s)
    s = re.sub(r'([!.?])', r' \1', s)
    s = re.sub(r'[^a-zA-Z.,ƆɔɛƐ!?’\'\"\\]+', r'', s)
    s = re.sub(r'\s+', r' ', s)
    return s


'''Find all matches of words with special characters and clean them'''
def findall(s):
    match = []
    for idx, word in enumerate(s):
        for x in word:
            if x in ['Ↄ','Ɔ','ɔ','ↄ','ᴐ','ɛ','Ɛ','ε']:
                match.append(s.pop(idx))
    # xx = re.findall(r'([ↃƆɔↄᴐɛƐ])', ' '.join(s)) # Find all matches of \ special characters
    clean = replace(match)
    return s + clean

'''Cleaning'''
def replace(s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j != 0:
                if s[i][j] == 'Ͻ' or s[i][j] == 'ɔ':
                    t = list(s[i])
                    t[j] = 'ɔ'
                    s[i] = ''.join(t)
                elif s[i][j] == 'ɛ' or s[i][j] == 'ɛ':
                    t = list(s[i])
                    t[j] = 'ε'
                    s[i] = ''.join(t)
    return s


def main():
    '''Open text file'''
    with open('tw.txt') as f:
        data = f.readlines()
    x = findall(data)

    '''Save cleaned text'''
    with open('tw1.txt', 'w') as f:
        f.write(''.join(x))


if __name__ == "__main__":
    main()
