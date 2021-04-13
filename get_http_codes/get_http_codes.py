#!/bin/env python
"""
get_http_codes.py
Purpose: reads https access log, and prints occurences of codes
Usage:
    -f|--file       file name

Examples:
    python get_http_codes.py  -f access.log
Author: Dovi Klausner
Date: 04/2021
"""

import argparse
from apachelogs import LogParser
import json


def parse_parameters():
    """Parse the command line parameters and return the args dictionary."""
    parser = argparse.ArgumentParser(description="Search Http Codes Tool")
    parser.add_argument('-f', '--file', type=str, required=True, help="file name")
    args = parser.parse_args()
    return args

def search_codes(file):
    codes_amount = {}
    parser = LogParser("%h %l %u %t \"%r\" %>s %b")

    #Full syntax:
    #parser = LogParser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    #more documentation at: https://pypi.org/project/apachelogs/

    with open(file) as f:
        mylist = list(f)

    for line in mylist:
        current_log = ' '.join(line.split())
        entry = parser.parse(current_log)
        current_code = entry.final_status

        if current_code not in codes_amount:
            codes_amount[current_code] = 1
        else:
            codes_amount[current_code] += 1

    return codes_amount

def main():
    args = parse_parameters()
    #print args
    #print args.file
    codes_amount = search_codes(args.file)
    print("https codes occurrences:")
    #print(codes_amount)
    print(json.dumps(codes_amount,indent=4))


if __name__ == '__main__':
    main()
