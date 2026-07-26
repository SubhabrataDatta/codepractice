#!/usr/bin/python
#Script scans log file and prints 1st line and lines containg "git"

#Path passed from bat to python using sys.argv[1]
#sys.argv[0] script name itself
#sys.argv[1] = first value passed

import sys
filepath = sys.argv[1]

#open(filepath, "r")	Opens file for reading
#with ... as f:	Auto-closes the file when done (good practice)
#f.readlines()	Reads ALL lines into a list
#lines[0]	First line (Python lists start at 0)

with open(filepath, "r") as f:
    lines = f.readlines()

#print first line and lines with git

if lines[0]:
    print(lines[0])
for line in lines:
    if "git" in line:
        print(line)
        
print(f"Log Summary Completed for {filepath}")