import unicodedata
import re


def unicode_to_ascii(s):
    return ''.join(
        c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')


def normalize_twi(s):
    s = unicode_to_ascii(s)
    s = re.sub(r'([!.?])', r' \1', s)
    s = re.sub(r'[^a-zA-Z.,ƆɔɛƐ!?’\'\"\\]+', r'', s)
    s = re.sub(r'\s+', r' ', s)
    return s


def findall(s):
    t = []
    for idx, word in enumerate(s):
        for x in word:
            if x in ['Ↄ','Ɔ','ɔ','ↄ','ᴐ','ɛ','Ɛ','ε']:
                t.append(word)
    # xx = re.findall(r'([ↃƆɔↄᴐɛƐ])', ' '.join(s)) # Find all matches of special characters
    # tt = replace(t)
    # return s + tt
    return xx


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
    return x


    '''Save cleaned text
    with open('tw1.txt', 'w') as f:
        f.write(''.join(x))
    '''

if __name__ == "__main__":
    x = main()
    #t = replace(x)
    #print(len(t))
    print(x)
    #print(x[0:100])
    # print(t[1])
