import os
import re
from fire import Fire


def generate_lmdb(path):
    if path.endswith('/'):
        path = path.rstrip('/')
    p = os.listdir(path)
    names = []
    for i, x in enumerate(p):
        idx = [i.start() for i in re.finditer('_', x)]
        idx = idx[-1]
        label = x[:idx]
        src = f'{path}/{x}'
        target = f'{path}/word_{i+1}.jpg'
        os.rename(src, target)
        t = f'{target}\t{label}\n'
        names.append(t)

    with open('gt.txt', 'w') as f:
        f.writelines(names)


if __name__ == '__main__':
    Fire(generate_lmdb)
