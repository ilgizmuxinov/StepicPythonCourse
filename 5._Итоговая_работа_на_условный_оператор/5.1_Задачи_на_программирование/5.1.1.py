a = int(input())
if 1 <= a // 100 <= 9 and a % 100 == 0 and a % 10 == 0:
        print('YES')
elif 1 <= a // 1000 <= 3 and a % 100 == 0 and a % 10 == 0:
        print('YES')
else:
    print('NO')
