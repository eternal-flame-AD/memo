import csv
import codecs


def readcsv(fn):
    readfile = open(fn)
    return csv.DictReader(readfile)
