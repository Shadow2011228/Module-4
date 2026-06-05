# В словаре вместо индексом используются ключи
#         ключ1     ключ2       ключ3        ключ4         ключ5      ключ6      ключ7
dict1 = {'key1':1, 'key2':2.1, 'key3':True, 'key4':'123', 'key5':[], 'key6':(), 'key7':{}} # Создали словарь
print(dict1)

print(dict1['key1'], "Получили 1-ое значение по ключу 'key1'")

dict1['new key'] = 'new elem'
print(dict1, 'Добавили новый элемент в конец словаря')

dict1.update({'new dict':123})
print(dict1, 'Склеили 2 словаря')

dict1.pop('new dict')
print(dict1, 'Удалили элемент - \'new dict\'')

del dict1['new key']
print(dict1, 'Удалили элемент - \'new key\'')

del dict1
# print(dict1)

dict1 = {'key1':1, 'key2':2.1, 'key3':True, 'key4':'123', 'key5':[], 'key6':(), 'key7':{}}

for key in dict1: # Цикл for кладет в свою переменную ключи словаря
    print(key, dict1[key])

for item in dict1.items(): # Метод .items() возвращает кортежи с ключами и значениями
     print(item)

for value in dict1.values(): # Метод .values() возвращает только значения
    print(value)

dict1_keys = list(dict1.keys()) # Метод .keys() возвращает только ключи
print(dict1_keys)