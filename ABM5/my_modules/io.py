# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 18:29:42 2023

@author: 肉松
"""

import csv

# Read input data
def read_data():
    f = open('../../data/input/in.txt', newline='')
    data = []
    n_rows=0
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        n_cols=0
        n_rows=n_rows+1
        for value in line:
            row.append(value)
            n_cols=n_cols+1
            #print(value)
        data.append(row)
    f.close()
    print(data)
    return n_cols, n_rows, data
    


