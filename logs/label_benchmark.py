# This is a python script that is used for find the right label for the benchmark 
#and add the new unified memory advise into the benchmark cuda code
import csv
import glob

def isfloat(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True

lineList = list()
with open("label.txt") as f:
  for line in f:
      value = line.split(' ')
      #value = line.split(' ')[-1]
      length_of_value = len(value)
      if isfloat(value[length_of_value-1]) : #value[length_of_value-1].isdigit():
          if value[length_of_value-1] != ' ':
                print value[length_of_value-8].split(':')[1], value[length_of_value-1]
      #if length_of_value > 14 :
           # print value[30]
    #lineList.append(line)