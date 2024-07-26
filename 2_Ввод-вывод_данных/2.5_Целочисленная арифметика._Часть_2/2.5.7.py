num = int(input())
dig3 = num % 10
dig2 = (num // 10) % 10
dig1 = (num // 10) // 10
print("Сумма цифр =", dig3 + dig2 + dig1)
print("Произведение цифр =", dig3 * dig2 * dig1)
