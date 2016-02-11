# pytime
###https://github.comi/aubsec/pytime.git

<p>The purpose of this Python project is to replicate functions of the mactime perl 
script in Python-3 while modifying some of the output.  It also personally serves 
as practice in programming in Python-3 and utilizing vim.</p> 

<p>pytime generates timelines from a body file.  Body files can be generated from
a number of other applications, most commonly from the TSK fls, log2timeline,
and from volatility. </p>


## Usage

<p>pytime takes up to three arguments.  The argument -b must be used to identify
the body file to be parsed.  Optionally the -s and -e arguments can be used to
specify a start and end date using the date format of "YYYY-MM-DD". </p>

<p>A Start [-s] date and End [-e] date can be specified in format "YYYY-MM-DD".  If no
date arguments are specified, the program will parse all data in the body file (Example 1).  
If only the start date is specified, it will parse all data from the start date to the 
end of the file (Example 2).  If the end date is specified, it will parse all data from the 
beginning of the file to the specified end date (Example 3).  If both a start and end date is 
specified, only dates between the start and endl will be parsed (Example 4).
</p>
<br>
<br>Example 1:  pytime -b bodyfile.body
<br>Example 2:  pytime -b bodyfile.body -s 2016-01-01
<br>Example 3:  pytime -b bodyfile.body -e 2016-02-01
<br>Example 4:  pytime -b bodyfile.body -s 2016-01-01 -e 2016-02-01
<br>
<br>optional arguments:
  <br>-h, --help                 show this help message and exit
  <br>-b BODY, --body BODY      Input body file
  <br>-s START, --start START   Optional. Input the Start Date in format "YYYY-MM-DD"
  <br>-e END, --end END             Optional. Input the End Date in format "YYYY-MM-DD

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

Matthew Aubert
-@aubsec
-aubsec@gmail.com
-github.com/aubsec

## License

<p>pytime.py Used for timeline creation in digital investigations.</p>
<p>Copyright (C) 2016 Matthew Aubert<p>

<p>This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.</p>

<p>This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.</p>

<p>You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.</p>
