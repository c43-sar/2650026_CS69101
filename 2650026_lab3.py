import sys
arr0 = []
data0 = open("lab1_data0.dat", 'r')

try:
    for line in data0.readlines():
        line_data = line.rstrip().split(',') #using rstrip to remove the \n
        for data in line_data:
            arr0.append(int(data))
except:
    sys.exit("[ERROR] Invalid data")

print(arr0)