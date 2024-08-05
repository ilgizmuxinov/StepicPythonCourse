a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
if b1 - a1 == b2 - a2 or b1 - a1 == a2 - b2:
    print('YES')
elif (b1 == a1 and (1 <= (b2 - a2) or (a2 - b2) <= 7)) or (b2 == a2 and (1 <= (b1 - a1) or (a1 - b1) <= 7)):
    print('YES')
else:
    print('NO')
