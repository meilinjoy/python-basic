#!/usr/bin/python3
import urllib.request
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt'
filename = 'Example1.txt'
urllib.request.urlretrieve(url, filename)

with open("./Example1.txt","r") as File:
    #file_stuff = File.read()  #if use .read() and .readlines() together, the latter one will not get values
                            # the reason (I think) maybe when read()is done, the file has been closed
    #print(file_stuff)

    #file_stuff1 = File.readlines()
    #print (file_stuff1)
    #for file in file_stuff1:
    #    print(file,'---')

    file_stuff2 = File.read(5)
    print(file_stuff2,'999')
    file_stuff2 = File.readline()
    print(file_stuff2,'999')
