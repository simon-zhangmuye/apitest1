# coding=utf-8
__author__ = 'Simon Zhang'
__date__ = '2019/4/14 23:14'

import sys
import time
from math import sqrt


PW = 5209527

def is_prime(n):
    for i in range(3, int(sqrt(n))+2, 2):
        if n % i == 0:
            return False
    return True


class ProgressBar:
    def __init__(self, total=0, width=20):
        self.total = total
        self.width = width

    def show(self, count, done='#', wait='-'):
        proc = self.width * count // self.total
        ok, undo = done * proc, wait * (self.width - proc)
        print(f'\rRunning... [{ok}{undo}] {count}/{self.total}', end='')


def main(total=PW):
    start = time.time()
    n = 3
    bar = ProgressBar(total)
    for p in range(2, total):
        while True:
            n += 2
            if is_prime(n):
                bar.show(p + 1)
                break

    end = time.time()
    print(f'\ncost: {end-start} sec, result: {n}')


if __name__ == '__main__':
    main()
