import argparse
import re
import time
import os, sys

prime = [99371, 199933, 333667, 391939, 502669]

def sort_prime_array(prime):
    a = []
    b = 2
    while len(a) < prime:
        a.append(b)
        b = (b * 2) % prime
    sorted(a)


def block():
    for number in prime:
        sort_prime_array(number)

def test_sort(count):
    times = []
    for i in range(count):
        t0 = time.time()
        block()
        t1 = time.time()
        times.append(t1 - t0)
    return sum(times)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--piacin', dest='piacin', action='store_const', const=True, default=False, help='Use piacin')
    parser.add_argument('--clear', dest='clear', action='store_const', const=True, default=False, help='Clear piacin bag')
    parser.add_argument("-k", "--bmnumber", type=int, default=100, help="Number of time to repeat benchmark within run (default: 100)")

    args = parser.parse_args()

    if args.piacin:
        import piacin.hc

    print(test_sort(args.bmnumber))