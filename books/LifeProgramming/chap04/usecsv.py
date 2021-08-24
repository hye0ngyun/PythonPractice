import csv, os, re

def open_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        output = []
        for i in reader:
            output.append(i)
    return output

def write_csv(filename, the_list):
    with open(filename, 'w', newline='') as f:
        csvobject = csv.writer(f, delimiter=',')
        csvobject.writerows(the_list)

def switch(listname):
    for i in listname:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass