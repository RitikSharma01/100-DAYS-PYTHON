# with open("weather-data.csv") as file:
# data = file.readlines()
# print(data)
# #
# import csv

# with open("weather-data.csv")as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
#     print(temp)

import pandas

# data = pandas.read_csv("weather-data.csv")
# print(type(data))
# print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)


# data_list = data['temp'].to_list()
# total_temp = sum(data_list)
# print(f"total temp= {total_temp/len(data_list)}")

# print(f"Mean Temp: {data['temp'].mean()}")
# print(f"Max Temp: {data['temp'].max()}")


# print(data[data['day'] == 'Monday'])


# print(data[data['temp'] == data['temp'].max()])


# monday = data[data.day == 'Monday']

# temp_cel = 32+int(monday.temp)*9/5
# print(temp_cel)


data_squrial = pandas.read_csv('squirrel-data.csv')
gray = data_squrial[data_squrial['Primary Fur Color'] == 'Gray'].X.count()
cinnamon = data_squrial[data_squrial['Primary Fur Color']
                        == 'Cinnamon'].X.count()
black = data_squrial[data_squrial['Primary Fur Color'] == 'Black'].X.count()
# print(gray)
# print(cinnamon)
# print(black)

dict_squirral = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray, cinnamon, black]
}

data = pandas.DataFrame(dict_squirral)
data.to_csv('sqirral_color.csv')
