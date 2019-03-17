#!/bin/env python

import sys, re
import traceback
import argparse
import logging
import os

def parse_parameters():
    """Pars the command line parameters and return the args dictionary."""
    parser = argparse.ArgumentParser(description="Search Regex Tool")
    parser.add_argument('-r', '--regex',
                        action="store",
                        help="regex",
                        required=True)
    parser.add_argument('-f', '--files', 
                        type=argparse.FileType('r'), 
                        nargs='*',
                        help="List of files, separated by space, default is STDIN",
                        default=[sys.stdin])

    args = parser.parse_args()
    return args


def search_regex(reg, file):
    pattern = re.compile(reg)
    for i, line in enumerate(file):
        for match in re.finditer(pattern, line.strip()):
            print 'Found on line %s, column %s : %s' % (i+1, match.start(0)+1, line.strip())
    

def main():
    args = parse_parameters()
    #print args.regex
    for f in args.files:
        #print f
        search_regex(args.regex,f)


if __name__ == '__main__':
    main()
