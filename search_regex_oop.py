#!/bin/env python
"""
search_regex_other.py
Purpose: searches for lines matching regular expression within files/STDIN
Usage:
    -r|--regex          Regular expression to search
    -f|--files          List of files, separated by space, (default is STDIN)
    -u|--underscore     Prints '^' under the matching text. (Default false)
    -c|--color          highlight matching text. (Default false)
    -m|--machine        Generate machine readable output. (Default false)
                        Format: file_name:line_no:start_pos:matched_text
Examples:
    python search_regex_other.py -r '\d+' -f file1.txt file2.txt
    python search_regex_other.py -r '\d+' -f file1.txt file2.txt -m
    python search_regex_other.py -r '\d+' -f file1.txt file2.txt -u -c
    python search_regex_other.py -r '\d+' -f file1.txt file2.txt -uc
    echo "Some stdin output 123" | python search_regex_other.py -r '\d+' -uc
Author: Dovi Klausner
Date: 17/03/2019
This is one object oriented programming:
Following command pattern, which uses interface class
and implementing classes, all with same method names.
Error handling:
in case someone uses only BasePrint class, it'll raise NotImplementedError
"""
import sys
import re
import argparse

red_color = "\033[31m"
end_color = "\033[m"


class BasePrint(object):
    """Interface class,
       using factory to encapsulate differences  between output"""
    def __init__(self, lines, underscore=False):
        self._lines = lines
        self._underscore = underscore

    def __str__(self):
        raise NotImplementedError

    def factory(lines, machine=False, underscore=False):
        if machine:
            return FormatPrint(lines, underscore)
        if not machine:
            return HumanPrint(lines, underscore)
        assert 0, "Bad shape creation: " + type
    factory = staticmethod(factory)


class HumanPrint(BasePrint):
    """Print in "human" format"""
    def __str__(self):
        printStr = ""
        for line in self._lines:
            printStr = printStr + 'File %s, line %s, column %s : %s' % \
                  (line[0], line[1], line[2], line[3]) + '\n'
            if self._underscore:
                position = len('File ' + line[0] + ', line ' +
                               str(line[1]) + ', column ' + str(line[2]) +
                               ' : ') + line[2] - 1
                printStr = printStr + "".ljust(position) + '^\n'

        return printStr.strip()


class FormatPrint(BasePrint):
    """Print in below format:
    file_name:line_num:start_pos:matched_text"""
    def __str__(self):
        printStr = ""
        for line in self._lines:
            printStr = printStr + (str(line[0]) + ':' + str(line[1]) + ':' +
                                   str(line[2]) + ':' + str(line[3])) + '\n'

        return printStr.strip()


def parse_parameters():
    """Parse the command line parameters and return the args dictionary."""
    parser = argparse.ArgumentParser(description="Search Regex Tool")
    parser.add_argument('-r', '--regex', action="store",
                        help="Regular expression to search in files/STDIN",
                        required=True)
    parser.add_argument('-f', '--files', type=argparse.FileType('r'),
                        nargs='*', default=[sys.stdin],
                        help="List of files, separated by space, \
                              default is STDIN")
    parser.add_argument('-u', '--underscore', action="store_true",
                        help="Prints '^' under the matching text. \
                              Default false",
                        default=False)
    parser.add_argument('-c', '--color', action="store_true",
                        help="Highlight matching text. Default false",
                        default=False)
    parser.add_argument('-m', '--machine', action="store_true",
                        help="Generate machine readable output. Default false",
                        default=False)

    args = parser.parse_args()
    return args


def search_regex(reg, file, color=False):
    """Returns a list of lists
       each inner list represents a line with the regex in it:
       file name, line number, column number, line itself."""
    arr = []
    pattern = re.compile(reg)
    for i, line in enumerate(file):
        for match in re.finditer(pattern, line.strip()):
            if color:
                text = line[:match.start(0)] + red_color + \
                       line[match.start(0):match.end(0)] + \
                       end_color + line[match.end(0):]
            else:
                text = line
            arr.append([file.name, i+1, match.start(0)+1, text.strip()])
    return arr


def main():
    args = parse_parameters()
#    print args
#    print args.regex
    lines_arr = []
    for f in args.files:
        lines_arr += search_regex(args.regex, f, args.color)

    linesPrint = BasePrint.factory(lines_arr, args.machine, args.underscore)
    print linesPrint


if __name__ == '__main__':
    main()
