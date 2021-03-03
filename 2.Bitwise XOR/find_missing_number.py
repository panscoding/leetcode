"""
https://www.educative.io/courses/grokking-the-coding-interview/RLPGq6Vx0YY
"""
import os
import sys


def find_missing_number_brute_force(arr):
    n = len(arr) + 1

    s1 = 0
    for i in range(1, n+1):
        print(i)
        s1 += i

    for j in arr:
        s1 -= j

    return s1

def find_missing_number(arr):
    n = len(arr) + 1

    s1 = 1
    for i in range(2, n+1):
        s1 ^= i

    s2 = arr[0]
    for j in range(1, n-1):
        s2 ^= arr[j]

    return s1 ^ s2

def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is:' + str(find_missing_number(arr)))

if __name__ == "__main__":
    main()