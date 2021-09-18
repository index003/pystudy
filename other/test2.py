import re

def replace_temp(datas):
    for data in datas:
        with open('temp.json', 'r') as fout:
            alllines = fout.readlines()
        with open('temp.json', 'w+') as fin:
            for eachline in alllines:
                a = re.sub('783', 'data', eachline)
                fin.writelines(a)