# Duy Lam (ID: 61502602)
# Python Programming - Partner Project

# this project is one that can search for files in a directory
# (and all of its subdirectories, and their subdirectories, and so on)
# with interesting characteristics and take some kind of action on those files.

# 09/28/15

# Your program will take input from the console in the following format. It
# should not prompt the user in any way; it should simply read whatever input
# is typed into the console, and you should assume that your user knows the
# precise input format. A description of that format follows.

# 1. The first line of the input is the path to the directory in which the search
# for files should be rooted. For example, a Windows user might type C:\Program
# Files or D:\Python34\Lib, in which case only files in or "underneath" the chosen
# directory will be found.

#   If the first line of the input is not a valid path to a directory (e.g., not a path
#   to a directory that exists, or is not a valid path at all), print the word ERROR on
#   a line by itself and repeat reading a line of input; continue until the input is a
#   valid path to a directory.

# 2. The second line of the input specifies the search characteristics that will be
# used in deciding whether files are "interesting" and should have action taken on
# them. There are three different search characteristics; the second line of the
# input chooses one of them.

#   If the second line of the input begins with the letter N, the search will be
#   for files whose names exactly match a particular name. The N will be followed
#   by space; after the space, the rest of the line will indicate the name of the
#   files to be searched for.

#   If the second line of the input begins with the letter E, the search will be
#   for files whose name end in a particular extension. The E will be followed by
#   a space; after the space, the rest of the line will indicate the desired extension.

#       For example, if the desired extension is py, all files whose names end in .py
#       will be considered interesting. The desired extension may be specified with or
#       without a dot preceding it (e.g., E .py or E py would mean the same thing in
#       the input), and your search should behave the same either way.

#       Note, also, that there is a difference between what you might call a name ending
#       and an extension. In our program, if the search is looking for files with the
#       extension oc, a file named iliveinthe.oc would be found, but a file named
#       invoice.doc would not.

#   If the second line of the input begins with the letter S, the search will be for files
#   whose size, measured in bytes, strictly exceeds (i.e., is greater than) a specified threshold.
#   The S will be followed by a space; after the space, the rest of the line will be a non-negative
#   integer value specifying the size threshold.

#       For example, the input S 2097151 means that files whose sizes are at least 2,097,152
#       bytes (i.e., greater than 2,097,151 bytes) will be considered interesting.

#   If the second line of the input does not match one of the formats described above, print the
#   word ERROR on a line by itself and repeat reading a line of input; continue until the input is
#   a valid path to a directory.


# 3. The third line of the input specifies the action that should be taken on each of the interesting
# files found in the search. No matter what, you should always print the file's path, on its own line
# of output, to the console when you find an interesting one; the action chosen here specifies what
# else should be done with it.

#   If the third line of the input contains the letter P by itself, print the file's path to the
#   console — just as you will always do — but otherwise don't do anything with it.

#   If the third line of the input contains the letter F by itself, open the file under the
#   assumption that the file is a text read, read the first line of text from the file, and
#   print that text to the console. (If the file does not contain text, it's fine if this choice
#   prints unreadable garbage or even crashes your program; testing that a file is a text file is
#   trickier than it sounds, so we'll only test this feature on text files.)

#   If the third line of the input contains the letter D by itself, make a duplicate copy of the file and
#   store it in the same directory where the original resides, but the copy should have .dup
#   (short for "duplicate") appended to the filename. For example, if the interesting file is C:\pictures\boo.jpg,
#   you would copy it to C:\pictures\boo.jpg.dup.

#   If the third line of the input contains the letter T by itself, "touch" the file, which means to modify
#   its last modified timestamp to be the current date/time.


import os
import shutil
from pathlib import Path

def Command(Lst:[list]):
    #print(Lst)
    test = True
    while (len(Lst) != 0) and (test != False):
        userInput = input('3rd Input: ')
        userInput = userInput.strip()
        if userInput.upper() == 'P':
            print (Lst[:])
            #for element in Lst:
                #print(Path(element) , end = '\n')
            test = False
        elif userInput.upper() == 'F':
            for element in Lst:
                #print(element)
                directory = str(element)
                infile = open(directory , 'r')
                print(infile.readline())
                infile.close()
                #with element.open('r') as sample:
                 #   sample.readline()
                  #  element.close()
                #directory = str(Path(element))
                #new = open(directory, 'r')
                #print((new.readline()))
            test = False
        elif userInput.upper() == 'D':
            for element in Lst:
                #print('need to copy')
                source = str(element)
                #print(source)
                shutil.copyfile(source, source + '.dup')
            test = False
        elif userInput.upper() == 'T':
            for element in Lst:
                os.utime(str(element),)
            test = False
                
        else:
            print('ERROR')
            userInput = input('3rd Input: ')
            userInput = userInput.strip()
    return


def Directory() -> str:
    directoryInput = None
    userInput = str(input("Please enter  the path to the directory in which the search for files should be rooted:"))
    while (directoryInput == None):
        if (Path(userInput).is_dir()):
            directoryInput = userInput
        else:
            print('ERROR')
            userInput = (input("Please enter  the path to the directory in which the search for files should be rooted:"))
    #print (directoryInput)
    return directoryInput
    
def categorizedSearch(DirectoryInput):
    Directory = (DirectoryInput)
    returnLst = None
    #print('a')
    #print(Path(DirectoryInput))
    searchPref = input("Please enter search preference:")
    while (returnLst == None):#(searchPref != '') and 
        searchPref = searchPref.strip()
        if searchPref[0:1].upper() == "N":
            fileName = searchPref[2:(len(searchPref))]
            DirsFilesLst = sorted(Path(Directory).glob('**/*'))
            filesLst = list()
            for element in DirsFilesLst:
                if element.is_file() and element.match(fileName):
                    filesLst.append(element)
            if len(filesLst) > 0:
                print(filesLst[:])
                returnLst = filesLst[:]
            else:
                    print(fileName + ' is not a valid filename under specified path')
                    returnLst = []
                    
        elif searchPref[0:1].upper() == "E":
            fileExtension = searchPref[2:(len(searchPref))]
            Extension = fileExtension.strip('.').strip()
            Extension = '.' + Extension
            DirsFilesLst = sorted(Path(Directory).glob('**/*'))
                
            ExtLst = list()
            for element in DirsFilesLst:
                if (element.suffix == (Extension)) and element.is_file():
                    ExtLst.append(element)
            if len(ExtLst) > 0:
                print(ExtLst[:])
                returnLst = ExtLst[:]
            else:
                print('there is not a file under the extension: ' + fileExtension)
                returnLst = []
                    
        elif (searchPref[0:1].upper() == "S" and searchPref[2:].strip().isdigit()):
            size = searchPref[2:]
            size = int(size)
            print(size)
            allDirs = sorted(Path(Directory).glob('**/*'))
            foundDirs = list()
            for element in allDirs:
                if ((element.stat().st_size > size) and Path(element).is_file() and len(allDirs)> 0):
                    foundDirs.append(element)
                else:
                    print('.' , end= ' ')
            print(foundDirs[:])
            returnLst = foundDirs[:]
            
        else:
            print('ERROR Else')
            searchPref = input("Please enter search preference:")
    return returnLst


if __name__ == "__main__":
    n = Directory()
    print(n)
    print(n)
    
    a = categorizedSearch(n)
    #print ('a')
    Command(a)



        
