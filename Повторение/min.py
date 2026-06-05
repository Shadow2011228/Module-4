
numbers = [34, 2, 15, 67, 89, 1, 45, 103, 7, 23]

print("Список чисел", numbers)


min_number = numbers[0]

for num in numbers:
    if num < min_number:
        min_number = num

print("Самое маленькое число в списке:", min_number)