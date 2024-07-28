n1, n2, op = int(input()), int(input()), input()
if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/' and n2 == 0:
    print('На ноль делить нельзя!')
elif op == '/':
    print(n1 / n2)
else:
    print('Неверная операция')
