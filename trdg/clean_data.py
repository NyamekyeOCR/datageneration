import unicodedata
import re
from fire import Fire

blanks = ['', '\n']
special_char1 = [chr(390), chr(596), chr(7440), chr(8579), chr(8580)] #Character codes for all occurances of"ɔ"
special_char2 = [chr(400), chr(603), chr(949)] #Character codes for all coccurance of "ɛ"
special_chars = special_char1 + special_char2

'''
NOTE:
This is a script to clean your twi corpus. It takes in a file of your twi corpus with a word on a single line.
A crude  way since the special characters ᴐ and ɛ are sometimes not rendered in the images, we convert them to c and j respectively. This way everything is rendered since they are recognized in the fonts.
This does not work that efficiently so sometimes you would have to go into the file and ctrl+f and change some of them manually.

TODO:
    - Find ways to make the special characters ᴐ and ɛ to render directly.
    - Find ways to efficiently fix the changing of all special characters to c and j.
'''



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
    print('FINDING WORDS WITH SPECIAL CHARACTERS')
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
    return s + clean


'''Cleaning'''
def replace(s):
    for i, word in enumerate(s):
        if special_char1[0] in word:
            word = word.replace(special_char1[0], 'c')
        if special_char1[1] in word:
            word = word.replace(special_char1[1], 'c')
        if special_char1[2] in word:
            word = word.replace(special_char1[2], 'c')
        if special_char1[3] in word:
            word = word.replace(special_char1[3], 'c')
        if special_char1[4] in word:
            word = word.replace(special_char1[4], 'c')
        if special_char2[0] in word:
            word = word.replace(special_char2[0], 'j')
        if special_char2[1] in word:
            word = word.replace(special_char2[1], 'j')
        if special_char2[2] in word:
            word = word.replace(special_char2[2], 'j')
        s[i] = word

    return s


def main(input, output):
    '''Open text file'''
    print('----------------')
    print(f'READING INPUT FILE {input}')
    print('----------------')
    with open(input) as f:
        data = f.readlines()
    x = findall(data)

    '''Delete blank lines'''
    x = [line for line in x if line != '']

    print('----------------')
    print(f'SAVING TO OUTPUT FILE {output}')
    print('----------------')

    '''Save cleaned text'''
    with open(output, 'w') as f:
        f.write('\n'.join(x))

    print('----------------')
    print('DONE')
    print('----------------')


'''
Run script as
python clean_data.py --input=input_filename --output=output_filename
'''
if __name__ == "__main__":
    Fire(main)
