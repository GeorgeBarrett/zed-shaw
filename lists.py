list1 = ['physics', 'chemistry']
list2 = [1, 2, 3, 4, 5, 6, 7, 7]
list3 = ['red', 'green', 'green', 'green', 'blue']
list4 = ['tree', 'leaf', 5, 6, 10]
list5 = ['window', 5, 8, 'plant']
list6 = ['apple', 'banana', 'cherry', 'cherry']

# adding biology to list1
list1.append('biology')

# this is storing the amount of greens there are in list3 in a variable
colour_count = list3.count('green')

# this is storing the popped object in a variable
remove_last_object = list4.pop()

# this is storing the removed item in a variable
remove_object = list5.remove(8)

# this is counting the quantity of cherries in list6 and storing it as a variable
how_many_cherries = list6.count('cherry')





print(list1)
print(list2[1:5])
print('the count of colour green is', colour_count)
print(list4)
print(list5)
print(remove_last_object)
print(how_many_cherries)