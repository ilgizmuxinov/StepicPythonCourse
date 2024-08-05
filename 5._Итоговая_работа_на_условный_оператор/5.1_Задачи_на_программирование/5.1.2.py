a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if (a1 % 2 == 0 and a2 % 2 == 1) and ((b1 % 2 == 1 and b2 % 2 == 0) or (b1 % 2 == 0 and b2 % 2 == 1)):
    print('YES')
elif (a1 % 2 == 1 and a2 % 2 == 0) and ((b1 % 2 == 1 and b2 % 2 == 0) or (b1 % 2 == 0 and b2 % 2 == 1)):
    print('YES')
elif (a1 % 2 == a2 % 2 == 1) and ((b1 % 2 == b2 % 2 == 1) or (b1 % 2 == b2 % 2 == 0)):
    print('YES')
elif (a1 % 2 == a2 % 2 == 0) and ((b1 % 2 == b2 % 2 == 1) or (b1 % 2 == b2 % 2 == 0)):
    print('YES')
else:
    print('NO')