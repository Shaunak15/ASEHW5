import sys
sys.path.append("./src")
from typing import List
import csv
import copy as copy
import tests
from main import the
import update

def csv_content(src):
    res = []
    with open(src, mode='r') as file:
        csvFile = csv.reader(file)
        for row in csvFile:
            res.append(row)
    return res

class Data():
    

    ## constructor created for data.py class
    def __init__(self):
        self.cols = None
        self.rows = []


    def read_file(self, content):
        data = Data()
        callback_function = lambda t: update.row(data, t)
        tests.readCSV(content, callback_function)
        return data

    def clone(self, data, ts=None):
        data1 = update.row(Data(), data.cols.names)
        for t in ts or []:
            update.row(data1, t)
        return data1

        
