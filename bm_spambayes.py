#!/usr/bin/env python

"""Wrapper script for testing the performance of SpamBayes.

Run a canned mailbox through a SpamBayes ham/spam classifier.
"""

__author__ = "skip.montanaro@gmail.com (Skip Montanaro)"
__contact__ = "collinwinter@google.com (Collin Winter)"


# Python imports
import optparse
import os.path
import time
import argparse
import sys

# SpamBayes imports
from spambayes import hammie, mboxutils


def test_spambayes(iterations, messages, ham_classifier):
    # Prime the pump. This still leaves some hot functions uncompiled; these
    # will be noticed as hot during the timed loops below.
    for msg in messages:
        ham_classifier.score(msg)

    times = []
    for _ in range(iterations):
        t0 = time.time()
        for msg in messages:
            ham_classifier.score(msg)
        t1 = time.time()
        times.append(t1 - t0)
    return sum(times)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--piacin', dest='piacin', action='store_const', const=True, default=False, help='Use piacin')
    parser.add_argument('--clear', dest='clear', action='store_const', const=True, default=False, help='Clear piacin bag')
    parser.add_argument("-k", "--bmnumber", type=int, default=100, help="Number of time to repeat benchmark within run (default: 100)")
    args = parser.parse_args()


    # parser = optparse.OptionParser(
    #     usage="%prog [options]",
    #     description=("Run the SpamBayes benchmark."))
    # util.add_standard_options_to(parser)
    # options, args = parser.parse_args()

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    mailbox = os.path.join(data_dir, "spambayes_mailbox")
    ham_data = os.path.join(data_dir, "spambayes_hammie.pkl")
    msgs = list(mboxutils.getmbox(mailbox))
    ham_classifier = hammie.open(ham_data, "pickle", "r")

    # util.run_benchmark(options, options.num_runs, test_spambayes, msgs, ham_classifier)
    if args.piacin:
        import piacin.hc

    print test_spambayes(args.bmnumber, msgs, ham_classifier)
