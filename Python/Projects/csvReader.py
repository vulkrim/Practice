#!/usr/bin/python3

import csv

def readCSV(fileName):

    csvfile = open(fileName,'r')
    reader = csv.reader(csvfile)

    for row in reader:
        print(row)

def dictCSV(fileName):

    csvfile = open(fileName, 'r')
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
