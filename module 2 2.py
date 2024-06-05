first = int(input('Введите число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third and first == third:
    print(3)
elif first != second != third and first != third:
    print(0)
else:
    print(2)
