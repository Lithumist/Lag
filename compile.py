# created by Pedro Custodio

# command line utility that takes a javascript file
# as input, goes though it and replaces #include with
# the appropriate js files. Also minimises the resulting 
# large file and saves it.

# usage: compile.py file.js

# options:
# -m  minimised the resulting file.

import sys
import argparse

# handle arguments
parser = argparse.ArgumentParser( description="update this later pls" )
parser.add_argument( "filename" )
parser.add_argument( "-m", "--minimise", help="minimises the resultant file", action="store_true" )
parser.add_argument( "-o", "--output", help="filename of the resultant file" )
args = parser.parse_args()

# set options
optInputfile = args.filename
optMinimise = True if args.minimise else False
optOutputfile = args.output if args.output else "COMPILED_" + optInputfile

# extracts the next filename in double or single quotes from a position
def extract_filename ( string, position ):
    curPos = position
    curString = ""
    done = False
    inName = False
    while not done:
        if not inName:
            if string[curPos] == '"' or string[curPos] == "'":
                inName = True
        else:
            if string[curPos] != '"' and string[curPos] != "'":
                curString += string[curPos]
            else:
                done = True
        curPos += 1
        if curPos-position >= 40:
            # probably a missing " or '
            print( "COMPILE ERROR: #include filename too long. You've probably missed a ' or \"" )
            break
    return curString

# replaces everything with spaces in 'string' from 'position' until 2 ' or " are found
def replace_include_line ( string, position ):
    curPos = position
    done = False
    quoteCount = 0
    curLen = 0
    while not done:
        curLen += 1
        if string[curPos] == '"' or string[curPos] == "'":
            quoteCount += 1
        if quoteCount >= 2:
            done = True
        curPos += 1
    newString = string[:position-1] + string[position+curLen:]
    return newString

# inserts string 'b' into string 'a' at position 'pos'
def string_insert ( a, b, pos ):
    return a[:pos] + b + a[pos:]

# recursive file parsing function
def parse_file ( filename ):
    file = open( filename, 'r' )
    fileStr = file.read()
    count = 0
    pos = 0
    while True:
        # find the next include
        pos = fileStr.find( "#include", pos )
        if pos == -1: break
        # read the filename
        includeFilename = extract_filename( fileStr, pos )
        # remove the #include from file
        fileStr = replace_include_line( fileStr, pos )
        # insert the included file
        fileStr = string_insert( fileStr, parse_file( includeFilename ), pos ) # woah here's where the magic happens
    file.close()
    return fileStr
    

# parse file and save to file
file = open( optOutputfile, 'w' )
file.write( parse_file( optInputfile ) )
file.close()