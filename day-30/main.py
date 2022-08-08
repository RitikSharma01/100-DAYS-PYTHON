# # with open('a_file.text') as file:
# #     file.read()


# from importlib.resources import open_binary


# try:
#     file = open('a_foile.text')

# except:
#     print("there was a problem")
# # else

fruits = ['apple', 'pear', 'orange']


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + 'pie')
    except IndexError:
        print('fruit pie')
    else:
        print(fruit+'pie')


make_pie(4)
