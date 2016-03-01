#!/usr/bin/python

from sys import argv

script, filename1, filename2 = argv

#f1 = open(filename1, "r")
#f2 = open(filename2, "r")
outfile = open("merged.txt", "w")

id = {}
info = {}
with open(filename1, "r") as f1 :
	for line in f1:
		line = line.strip()
		col = line.split("\t")
		id[col[0]] = 1
		info[col[0]] = line
		
with open(filename2, "r") as f2 :
        for line in f2:
                col = line.split("\t")
		if col[0] in info.keys():
			newline = info[col[0]] + "####" + line
			outfile.write(newline)

f1.close()
f2.close()
outfile.close()
