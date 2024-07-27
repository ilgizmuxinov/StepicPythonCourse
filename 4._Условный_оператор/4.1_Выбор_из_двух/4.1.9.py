a = int(input())
b = int(input())
c = int(input())
if a > 0:
    s = a
else:
    s = 0
if b > 0:
    s = s + b
else:
    s = s
if c > 0:
    s = s + c
else:
    s = s
if s > 0:
    print(s)
else:
    print(0)
