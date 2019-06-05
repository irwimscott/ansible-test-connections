import csv
import sys

with open('list.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    for i, element in enumerate(readCSV,1):
        f = open("varfile_" + str(i) + ".yaml", 'w')
        sys.stdout = f
        print"host_src:", element[0]
        print"host_dst:", element[1]
        print"port_dst:", element[2]
        f.close()
