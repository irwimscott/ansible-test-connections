import csv
import sys

orig_stdout = sys.stdout
f = open('output.txt', 'w')
sys.stdout = f

print('access_vars:')
with open('lista.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=';')

    for i, element in enumerate(readCSV,1):
        print" - name: host", i
        print"   host_src:", element[0]
        print"   host_dst:", element[1]
        print"   port_dst:", element[2]

sys.stdout = orig_stdout
f.close()
