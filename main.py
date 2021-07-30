number_list = [32, 21, 48, 34.56]
print(number_list)
some_list = [12, 35.334, 'hello']
print(some_list)
print(len(some_list))
print(some_list[1])
another_list = some_list[:2]
print(another_list)
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list
print(new_list)
#adding items
new_list.append('new item')
new_list.insert(0, 'start')
new_list.insert(2,13)
print(new_list)
#removing items
new_list.pop(-1)
new_list.pop(0)
new_list.pop(-3)
deleted_item = new_list.pop()
print(new_list)
print(deleted_item)

my_list = [12, 'USA', 'Sun', 14, 'Mars', 12, 'Mars']
my_list.remove(12)  # удаляем элемент 12 в начале
print(my_list)

number_list1 = [45, 12, 3, -455, 22]
letter_list1 = ['s', 'w', 't', 'a']

number_list1.sort()
letter_list1.sort()

print(number_list1)
print(letter_list1)

number_list2 = [46, 13, 4, -456, 23]
number_list2.sort()
new_list1 = number_list2
print(new_list1)

number_list3 = [42, 12, 5, -450, 24]
number_list3.reverse()
print(number_list3)


number_list4 = [47, 10, 2, -458, 23]
letter_list4 = ['e', 'v', 'j', 'p']
number_list4.append(letter_list4)
print(number_list4)