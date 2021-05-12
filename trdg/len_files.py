import os
from fire import Fire


def len_files(src):
   return len(os.listdir(src))



def main():
    Fire(main)



if __name__ == '__main__':
    main()
