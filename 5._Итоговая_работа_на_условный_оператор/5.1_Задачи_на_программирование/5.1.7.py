a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if ((b1 - a1 == 1 or a1 - b1 == 1) and (b2 - a2 == 2 or a2 - b2 == 2)) or ((b1 - a1 == 2 or a1 - b1 == 2) and (b2 - a2 == 1 or a2 - b2 == 1)):
    print('YES')
else:
    print('NO')
