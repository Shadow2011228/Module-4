#        0   1    2      3    4   5   6 - индексы
list1 = [1, 2.1, True, '123', [], (), {}]

print(list1[0], "Получили 1-ый элемент с помощью индекса")
print(list1[1:4], 'Получили срез элементов от 2-го до 4-го')

list1.append('new elem')
print(list1, 'Добавили новый элемент в конце списка')

list1 += ['new list']
print(list1, 'Склеили 2 списка')

list1.remove('new list')
print(list1, 'Удалили элемент - \'new list\'')

del list1[1]
list1.pop()
list1.pop(0)
print(list1, 'Удалили первый, второй и последний элемент списка')

del list1
print(list1)

