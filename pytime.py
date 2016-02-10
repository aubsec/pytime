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
        return int(datetime.datetime.strptime(datestr, '%Y-%m-%d').timestamp())
    except:
        msg = "[!] Not a valid date: '{0}'.".format(datestr)
        raise argparse.ArgumentTypeError(msg)

def dateConvert(row):
    for i in range(len(row)):
        if i >= 7 and i <= 10:
            row[i] = datetime.datetime.fromtimestamp(int(row[i])).strftime('%Y-%m-%dT%H:%M:%S')
        else:
            continue
    return row  

#Sorts the CSV by the column 8 
def csvSorter(args):
    try:
        with open(args.body) as openfile:
            reader = csv.reader((x.replace('\0','') for x in openfile), delimiter='|')
            col = 8
            filteredrows = filter(lambda x: len(x) > col and x[col].isdigit(), reader)
            sortedreader = sorted(filteredrows, key=lambda k: k[col]) 
            csvOutput(sortedreader, args, col)
        return 0
    except Exception as errorvalue:
        function = 'csvSorter()'
        exceptionHandler(errorvalue, function)


#csvOutput parses the args.start and args.end.
#Prints rows from sortedreader to stdout until 
#args.end is reached or until end of sortedreader.
#! TD - Modify the csvout.writerow(row) to modify the format of the timestamp to ISO.
def csvOutput(sortedreader, args, col):
    try:
        csvout = csv.writer(sys.stdout, delimiter=',')
        csvout.writerow(['MD5','name','inode','mode_as_string','UID','GID','size','atime','mtime','ctime','crtime'])
#If args.start does not have a value and args.end does
#Write every row until args.end to stdout.
        if str(args.start) == 'None' and str(args.end) != 'None':
            for row in sortedreader:
                try:
                    if float(row[col]) <= args.end:
                        csvout.writerow(row)
                except:
                    continue
#If args.start does have a value and args.end does not.
#Write row to stdout starting from args.start until end of file.
        elif str(args.start) != 'None' and str(args.end) == 'None': 
            for row in sortedreader:
                try:
                    if float(row[col]) >= args.start:
                        csvout.writerow(row)
                except:
                    continue
#If both args.start and args.end have value.
#Write row to stdout from args.start and until row[col] is equal to end. 
        elif str(args.start) != 'None' and str(args.end) != 'None':
            for row in sortedreader:
                try:
                    if float(row[col]) >= args.start and float(row[col]) <= args.end:
                        csvout.writerow(row)
                except:
                    continue
#Default write everything in file. 
        else:
            for row in sortedreader:
                try:
                    csvout.writerow(dateConvert(row))
                except:
                    continue
            
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
    parser.add_argument('-b', '--body', help='Input body file', required=True)
    parser.add_argument('-s', '--start', help='Input the Start Date', type=dateFormat, required=False)
    parser.add_argument('-e', '--end', help='Input the End Date', type=dateFormat, required=False)
    args = parser.parse_args()
    #sys.stderr.write(str(args.start) + '\n')
    #sys.stderr.write(str(args.end) + '\n')
    
    try:
        csvSorter(args)
        sys.stderr.write('[+] Program completed sucessfully\n')
        exit(0)
    except Exception as errorvalue:
        function = 'main()'
        exceptionHandler(errorvalue, function)

if __name__=='__main__':
    main()
