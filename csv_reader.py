#!/usr/bin/env python
# (@)/csv_reader.py
# A very simple CSV file reader
# Type "./csv_reader.py <filename>" to read the CSV file
# - Open the file for reading
# - Read the header first
# - Read the rest of the rows
# - In case there is an error, raise an exception
# - After reading everything, print the header and the rest of the rows

from __future__ import print_function
import sys
import csv

# If command line parameter is not 1, there is a problem, so ask what the filename is
if len(sys.argv) != 2:
    print("What is the filename?")
    print("Usage: {scriptname} <filename>".format(scriptname=sys.argv[0]))
    sys.exit(1)

filename = sys.argv[1]

filedata = []

try:
    with open(filename) as f:
        reader = csv.reader(f)
        header = reader.next()
        filedata = [row for row in reader]
except csv.Error as e:
    print("Error reading CSV file at line {line_num}: {error}".format(line_num=reader.line_num, error=e))
    sys.exit(-1)

if header:
    print(header)
    print('=====================')

for datarow in filedata:
    print(datarow) 

