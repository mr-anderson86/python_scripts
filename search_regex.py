#!/bin/env python

import sys, re
import traceback
import argparse
import logging
import os

def parse_parameters():
    """Pars the command line parameters and return the args dictionary."""
    parser = argparse.ArgumentParser(description="Search Regex Tool")
    parser.add_argument('-r', '--regex', action="store",
                        help="Regular expression to search in files/STDIN", required=True)
    parser.add_argument('-f', '--files', type=argparse.FileType('r'), 
                        nargs='*', default=[sys.stdin],
                        help="List of files, separated by space, default is STDIN")
    parser.add_argument('-u', '--underscore', action="store_true",
                        help="Prints '^' under the matching text. Default false",
                        default=False)
    parser.add_argument('-c', '--color', action="store_true",
                        help="Highlight matching text. Default false",
                        default=False)
    parser.add_argument('-m', '--machine', action="store_true",
                        help="Generate machine readable output. Default false",
                        default=False)

    args = parser.parse_args()
    return args


def search_regex(reg, file, machine, underscore, color):
    pattern = re.compile(reg)
    for i, line in enumerate(file):
        for match in re.finditer(pattern, line.strip()):
            if color:
                text = line[:match.start(0)] + "\033[31m" + line[match.start(0):match.end(0)] + "\033[m" + line[match.end(0):]
            else:
                text = line
            if machine:
                print '%s:%s:%s:%s' % (file.name, i+1, match.start(0)+1, text.strip())
            else:                    
                print 'File %s, line %s, column %s : %s' % (file.name, i+1, match.start(0)+1, text.strip())
                if underscore:
                    position = len('File ' + file.name + ', line ' + str(i+1 )+ ', column ' + str(match.start(0)+1) + ' : ') + match.start(0)
                    print "".ljust(position) + '^'


def main():
    args = parse_parameters()
    #print args
    #print args.regex
    for f in args.files:
        #print f
        search_regex(args.regex,f, args.machine, 
                    args.underscore, args.color)


if __name__ == '__main__':
    main()
