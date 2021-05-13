import os
import shutil
from fire import Fire


def copy_files(src, dest, num_files):
    p = os.listdir(src)
    for i in range(num_files):
        src = f'{src}/{p[i]}'
        tgt = f'{dest}/{p[i]}'
        shutil.move(src, tgt)


def main():
    Fire(copy_files)




if __name__ == '__main__':
    main()

