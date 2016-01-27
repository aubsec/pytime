#!/usr/bin/env python3

#    pytime.py Used for timeline creation in digital investigations. 
#    Copyright (C) 2016 Matthew Aubert
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#imports
import argparse
import csv
import datetime
import sys

def dateFormat(datestr):
    try:
        return datetime.datetime.strptime(datestr, '%Y-%m-%d').timestamp()
    except:
        msg = "Not a valid date: '{0}'.".format(datestr)
        raise argparse.ArgumentTypeError(msg)

#Sorts the CSV by the column 8 and writes to out.csv using csv.writer
#Will convert timestamps to ISO before writing to out.csv.
def csvSorter(args):
    try:
        with open(args.body) as openfile:
            reader = csv.reader((x.replace('\0','') for x in openfile), delimiter='|')
            col = 8
            filteredrows = filter(lambda x: len(x) > col and x[col] is not None, reader)
            sortedreader = sorted(filteredrows, key=lambda k: k[col]) 
            csvOutput(sortedreader, args, col)
        return 0
    except Exception as errorvalue:
        function = 'csvSorter()'
        exceptionHandler(errorvalue, function)


#csvOutput parses the args.start and args.end.
#Prints rows from sortedreader to stdout until 
#args.end is reached or until end of sortedreader.
def csvOutput(sortedreader, args, col):
    try:
        csvout = csv.writer(sys.stdout, delimiter=',')
        if args.start == None and args.end == None:
            for row in sortedreader:
                try:
                    csvout.writerow(row)
                except:
                    continue

        elif args.start != None and args.end == None:
            for row in sortedreader:
                try:
                    if row[col] >= args.start:
                        csvout.writerow(row)
                    else:
                        break
                    continue
                except:
                    continue

        elif args.start != None and args.end != None:
            for row in sortedreader:
                try:
                    if row[col] >= args.start and row[col] < args.end:
                        csvout.writerow(row)
                    else:
                        break
                    continue
                except:
                    continue
        
        elif args.start == None and args.end != None:
            for row in sortedreader:
                try:
                    if row[col] <= args.end:
                        csv.out.writerow(row)
                    else:
                        break
                    continue
                except:
                    continue

        else:
            sys.stderr.write('[!] WTF!')
            return 1
    return 0
    except Exception as errorvalue:
        function = 'csvOutput()'
        exceptionHandler(errorvalue, function)

#exceptionHandler() collects error codes and prints to screen
def exceptionHandler(errorvalue, function):
    sys.stderr.write('[!] An error has occured in function ' + function + '\n')
    sys.stderr.write('[!] ' + str(errorvalue) + '\n')
    exit(1)

# Main
def main():
    parser = argparse.ArgumentParser(description='Generate timeline from body file.')
    parser.add_argument('-b', '--body', help='Input body file', required=False)
    parser.add_argument('-s', '--start', help='Input the Start Date', type=dateFormat, required=False)
    parser.add_argument('-e', '--end', help='Input the End Date', type=dateFormat, required=False)
    args = parser.parse_args()
    try:
        csvSorter(args)
        sys.stderr.write('[+] Program completed sucessfully\n')
        exit(0)
    except Exception as errorvalue:
        function = 'main()'
        exceptionHandler(errorvalue, function)

if __name__=='__main__':
    main()
