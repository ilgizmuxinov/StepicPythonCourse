a = int(input())
if a == 0:
    print('зеленый')
elif (1 <= a <= 10 or 19 <= a <= 28) and a % 2 == 0:
    print('черный')
elif (1 <= a <= 10 or 19 <= a <= 28) and a % 2 != 0:
    print('красный')
elif (11 <= a <= 18 or 29 <= a <= 36) and a % 2 != 0:
    print('черный')
elif (11 <= a <= 18 or 29 <= a <= 36) and a % 2 == 0:
    print('красный')
else:
    print('ошибка ввода')
