#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countSwaps function below.
def countSwaps(a):
    lastInd = len(a) - 1
    swapCount = int()

    def recur(a, swap=0):

        t = int()
        for ind in range(len(a)):
            if ind == lastInd:
                continue

            if a[ind] > a[ind + 1]:
                a[ind], a[ind + 1] = a[ind + 1], a[ind]
                swap += 1
                t += 1
        if t > 0:
            swap = recur(a, swap)

        return swap

    swapCount = recur(a)
    print(f"Array is sorted in {swapCount} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
