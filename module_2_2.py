print('Введите три числа: ')
number1, number2, number3 = input('Первое число: '), input('Второе число: '), input('Третье число: ')
print(number1, number2, number3)
#if number1 == number2 or number2 == number3 or number1 == number3: # вариант с оператором 'or'
if number1 == number2:
    print(2)
elif number2 == number3:
    print(2)
elif number3 == number1:
    print(2)
elif number1 == number2 == number3:
    print(3)
else:
    print(0)
