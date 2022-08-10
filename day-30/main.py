
# # exercise 1
# fruits = ['apple', 'pear', 'orange']


# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('Fruit pie')
#     else:
#         print(fruit + 'pie')


# make_pie(4)

# Excercise 2

# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Share': 1},
#     {'Likes': 33, 'Comments': 2, 'Share': 3},
#     {'Comments': 4, 'Share': 2},
#     {'Comments': 1, 'Share': 4},
#     {'Likes': 21, 'Comments': 2}
# ]
# total_likes = 0

# for post in facebook_posts:

#     try:
#         total_likes = total_likes + post['Likes']
#     except KeyError:
#         total_likes += 0

# print(total_likes)

# exercise 3 #

import pandas

data = pandas.read_csv('alphabet.csv')
phonatic_dict = {row.letter: row.code for(index, row) in data.iterrows()}
print(phonatic_dict)

a = True
while a:
    try:
        word = input("Enter a word: ").upper()
        output_list = [phonatic_dict[letter] for letter in word]
        a = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")

print(output_list)
