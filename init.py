#!/usr/bin/env python3
import os
import shutil
import subprocess
from random import randint, shuffle
from pathlib import Path

def main():
    comp = Path('data/comp')
    images = list(comp.glob('*.jpg'))
    shuffle(images)

    N = len(images)
    ntest = int(N  * 0.1)
    ntrain = N - ntest

    test = images[: ntest]
    train = images[ntest: ]

    assert len(test) == ntest
    assert len(train) == ntrain

    (comp / 'testA').mkdir()
    (comp / 'trainA').mkdir()

    for f in test:
        shutil.copy(str(f), str(comp / 'testA'))
    for f in train:
        shutil.copy(str(f), str(comp / 'trainA'))



    (comp / 'testB').mkdir()
    (comp / 'trainB').mkdir()

    def conv(src: str, dst: str):
        subprocess.run(['convert', src, '-colorspace', 'Gray', dst])

    for f in test:
        conv(str(f), str(comp / 'testB' / f.name))
    for f in train:
        conv(str(f), str(comp / 'trainB' / f.name))


if __name__ == '__main__':
    main()