import argparse
import time
import nltk
from nltk.corpus import wordnet
from nltk.corpus import gutenberg
from nltk import word_tokenize, sent_tokenize

from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.collocations import *

text = gutenberg.raw('austen-emma.txt')

def block():
	words = word_tokenize(text)

def test_tokenize(count):
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
		import piacin.ga

	print(test_tokenize(args.bmnumber))