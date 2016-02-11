README

Author:     Matthew Aubert, @aubsec, aubsec@gmail.com

Description:
The purpose of this Python application is to replicate
the function of the mactime perl script in Python 3 while
modifying some of the output.

usage: pytime.py [-h] -b BODY [-s START] [-e END]

Generates timeline from body file.  Body files can be originally generate from tools
like Log2Timeline, from The Sleuth Kit's fls, and even from volatility.  

A Start [-s] date and End [-e] date can be specified in format "YYYY-MM-DD".  If no
date arguments are specified, the program will parse all data in the body file (Example 1).  
If only the start date is specified, it will parse all data from the start date to the 
end of the file (Example 2).  If the end date is specified, it will parse all data from the 
beginning of the file to the specified end date (Example 3).  If both a start and end date is 
specified, only dates between the start and endl will be parsed (Example 4).  

Example 1:  pytime -b bodyfile.body
Example 2:  pytime -b bodyfile.body -s 2016-01-01
Example 3:  pytime -b bodyfile.body -e 2016-02-01
Example 4:  pytime -b bodyfile.body -s 2016-01-01 -e 2016-02-01

https://github.com/aubsec/pytime.git
https://twitter.com/aubsec

optional arguments:
  -h, --help            show this help message and exit
  -b BODY, --body BODY  Input body file
  -s START, --start START
                        Optional. Input the Start Date in format "YYYY-MM-DD"
  -e END, --end END     Optional. Input the End Date in format "YYYY-MM-DD"
