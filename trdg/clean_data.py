import unicodedata
import re
from fire import Fire
from time import time


blanks = ['', '\n']
special_char1_small = [chr(390), chr(596), chr(7440),chr(8580)] #Character codes for small "ɔ"
special_char1_big = [chr(1021), chr(8579)]  #Character codes for big "ɔ"
special_char2_big = [chr(400)] #Character codes for big "ɛ"
special_char2_small = [chr(603), chr(949)]  #Character codes for small "ɛ"
special_chars = special_char1_small + special_char1_big + special_char2_small + special_char2_big


# Illegal characters
illegal_chars = ["\\", "\/", "<", ">", "*", "?", "\"", "|", ":"]

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
    match = 0
    for idx, word in enumerate(s):
        for x in word:
            if x in special_chars:
                match += 1
                s[idx] = replace(s[idx])
                break
    print(f'Length of matched words: {match}')
    return s


'''Cleaning'''
def replace(s):
    for _, char in enumerate(s):
        if char in illegal_chars:
            s = s.replace(char, ' ')
        if char in special_char1_small:
            s = s.replace(char, 'c')
        if char in special_char1_big:
            s = s.replace(char, 'C')
        if char in special_char2_small:
            s = s.replace(char, 'j')
        if char in special_char2_big:
            s = s.replace(char, 'J')

    return s


def main(input, output):
    start = time()
    '''Open text file'''
    print('----------------')
    print(f'READING INPUT FILE {input}')
    print('----------------')
    with open(input) as f:
        data = f.readlines()
    x = findall(data)
    x = findall(x)

    '''Delete blank lines'''
    x = [line for line in x if line != '']

    print('----------------')
    print(f'SAVING TO OUTPUT FILE {output}')
    print('----------------')

    '''Save cleaned text'''
    with open(output, 'w') as f:
        f.write(''.join(x))

    print('----------------')
    print('DONE')
    print('----------------')

    end = time()
    print(f'Time: {end - start}')


'''
Run script as
python clean_data.py --input=input_filename --output=output_filename
'''
if __name__ == "__main__":
    Fire(main)
