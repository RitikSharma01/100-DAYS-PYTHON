# list = [1, 2, 3]
# new_list = [n+1 for n in list]
# print(f'New List:- {new_list}')
# newlist = [n*2 for n in range(1, 5)]
# for i in range(1, 5):
#     newlist.append(i*2)

# print(newlist)

list = ['Alex', 'Beth', 'Caroline', 'Dave', 'Elanor', 'FREddie']

new_list = [name.upper() for name in list if len(name) >= 5]

print(new_list)
