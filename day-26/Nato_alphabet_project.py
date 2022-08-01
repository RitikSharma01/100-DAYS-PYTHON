import pandas

data = pandas.read_csv('alphabet.csv')

# todo1 create a dictonary

data_dict = {raw.letter: raw.code for (index, raw) in data.iterrows()}
# print(data_dict)

name = input('Enter your name :- ').upper()

namelist = [value for value in name]
print(namelist)

answerlist = [data_dict[letter] for letter in namelist]
print(answerlist)
