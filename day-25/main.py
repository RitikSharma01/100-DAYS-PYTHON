# with open("weather-data.csv") as file:
# data = file.readlines()
# print(data)
#
import csv

with open("weather-data.csv")as data_file:
    data = csv.reader(data_file)
    temp = []
    for row in data:
        if row[1] != 'temp':
            temp.append(int(row[1]))
    print(temp)
