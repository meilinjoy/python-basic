#!/usr/bin/python3
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
with open('E:\python-project\python-advanced/test2.txt','a+') as File1:
   File1.write("This is BBB")