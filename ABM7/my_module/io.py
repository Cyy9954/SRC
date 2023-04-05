# -*- coding: utf-8 -*-

import csv

# Read input data
def read_data():
    f = open('../../data/input/in.txt', newline='')
    data = []#Initialize an empty list data to store the read data
    n_rows=0
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        #Initialize the variable n_cols to 0 and increment the variable n_rows by 1 each time a row is read
        row = []
        n_cols=0
        n_rows=n_rows+1
        for value in line:
            row.append(value)
            n_cols=n_cols+1
            #print(value)
        data.append(row)
    f.close()
    return n_cols, n_rows, data

def write_data(file, environment):
    f = open (file,'w')
    writer= csv.writer(f)
    writer.writerows(environment)