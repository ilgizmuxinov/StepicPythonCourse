x = int(input())
if (x % 7 == 0 or x % 17 == 0) and 1000 <= x <= 9999:
    print('YES')
else:
    print('NO')
