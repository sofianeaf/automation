# -*- coding: utf-8 -*-
import csv

def read_db_csv(file_name):
    with open(file_name) as csvDataFile:
        csvReader = csv.reader(csvDataFile)

        # store .csv in arr
        arr = []
        for row in csvReader:
            a = str(row).split(';', 21)
            # clean rows from undesires characters
            bad_chars = ['"', '[', ']', "'"]
            for i in range(len(a)):
                x = a[i]
                for j in bad_chars:
                    x = x.replace(j,'')
                a[i] = x
            arr.append(a)

        # get rid of the first rows
        del arr[0:5]
        del arr[len(arr)-1]

    return arr

def seperate_months(arr_in):
    # extract list of months
    month_lst = [item[0] for item in arr_in]
    for i in range(len(month_lst)):
        a = str(month_lst[i]).split('/', 3)
        month_lst[i] = a[0] + "/" + a[2]
    month_lst = list(set(month_lst))

    # seperate
    arr = []
    for i in range(len(month_lst)):
        a = str(month_lst[i]).split('/', 2)
        arr_ = []
        for j in range(len(arr_in)):
            b = str(arr_in[j][0]).split('/', 3)
            if b[0] == a[0] and b[2] == a[1]:
                arr_.append(arr_in[j])
        arr.append(arr_)

    return arr

src = read_db_csv('file.csv')
data = seperate_months(src)

"""
for i in src:
    for j in i:
        print(j)
    print("")
"""


for month in data:
    for line in month:
        fo_1 = line[4].find('LIDL')
        fo_2 = line[4].find('REWE')
        fo_3 = line[4].find('TOOGOODTOGO')

        in_1 = line[4].find('AFFES MOHAMED')

        fm_1 = line[4].find('Anis')

        fi_1 = line[4].find('Miete')
        fi_2 = line[4].find('OB-K541272659')

        bu_1 = line[4].find('Audible')
        bu_2 = line[4].find('AMZN')
        bu_3 = line[4].find('Amazon')
        bu_4 = line[4].find('TK Maxx Muenchen')

        if fo_1 != -1 or fo_2 != -1 or fo_3 != -1:
            print("-> food        ",line[14:22])
        elif in_1 != -1:
            print("-> income      ",line[14:22])
        elif fm_1 != -1:
            print("-> family      ",line[14:22])
        elif fi_1 != -1 or fi_2 != -1:
            print("-> fix expenses",line[14:22])
        elif bu_1 != -1 or bu_2 != -1 or bu_3 != -1 or bu_4 != -1:
            print("-> buy stuff   ",line[14:22])
        else:
            print(line[4],line[14:22])
    print()
