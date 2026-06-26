print("Придумайте любое число")
a = int(input())
ans = 50
max = 100
min = 100

while a != ans:
    answer = input(f'{ans} больше или меньше? ->')
    if answer == 'меньше':
        if min > ans // 2:
            min = ans // 2
        ans = ans-min
    else:
        if max > ans*2:
            max = ans*2
        ans = (max+ans)//2

print(f'Я угадал твое чилсо - {ans}')
