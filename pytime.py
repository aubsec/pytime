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
import sys
import csv

#Parses arguments.  If open(sys.argv[1] fails, generates error and exits.
#Sorts the CSV by the column 8 and writes to out.csv using csv.writer
#Will convert timestamps to ISO before writing to out.csv.
#May change the csv.writer to output to stdout.
def csvParser():
    try:
        with open(sys.argv[1]) as openFile:
            reader = csv.reader((x.replace('\0','') for x in openFile), delimiter='|')
            col = 8
            filteredRows = filter(lambda x: len(x) > col and x[col] is not None, reader)
            sortedReader = sorted(filteredRows, key=lambda k: k[col]) 
            csvout = csv.writer(sys.stdout, delimiter=',')
            for row in sortedReader:
                try:
                    csvout.writerow(row)
                except:
                    sys.stderr.write('[!] Error in row')
                    sys.stderr.write(row)
                    continue
     

        return 0
    except Exception as errorvalue:
        function = 'csvParser()'
        exceptionHandler(errorvalue, function)

#exceptionHandler() collects error codes and prints to screen
def exceptionHandler(errorValue, function):
    sys.stderr.write('[!] An error has occured in function ' + function + '\n')
    sys.stderr.write('[!] ' + str(errorValue) + '\n')
    usage()

#Prints usage information and exits
def usage():
    sys.stderr.write('[!] pytime.py requires only one argument, the source Body file\n[!] Output in CSV is to the standard out\n')
    sys.stderr.write('example:  pytime.py source.body\n')
    exit(1)

# Main
def main():
    try:
        csvParser()
        sys.stderr.write('[+] Program completed sucessfully\n')
        exit(0)
    except Exception as errorValue:
        function = 'main()'
        exceptionHandler(errorValue, function)

if __name__=='__main__':
    main()
