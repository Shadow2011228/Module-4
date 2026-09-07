x = input()
assert x.isnumeric(), "Нужно использовать только числа" # Принимает True или False и бросает ошибку AssertionError если False
print(int(x) + 100)

