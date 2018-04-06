import csv


def readcsv(fn):
    readfile = open(fn)
    return csv.DictReader(readfile)
