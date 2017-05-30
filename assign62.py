"""
62. convert .txt file in .json
"""
import csv
import json
with open('text.txt', 'rb') as csvfile:
    filereader = csv.reader(csvfile, delimiter='\t')
    i = 0
    header = []
    out_data = []
    for row in filereader:
        row = [elem for elem in row if elem]
        if i == 0:
            i += 1
            header = row
        else:
            _dict = {}
            for elem, header_elem in zip(row, header):
                _dict[header_elem] = elem
            out_data.append(_dict)
with open("file.jason",'w') as  jason:
    jason.write(json.dumps(out_data))

csvfile.close()
jason.close()
