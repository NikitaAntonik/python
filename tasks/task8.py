#Task 8
n = int(input("Введите ширину шоколадки: "))
m = int(input("Введите длину шоколадки: "))
k = int(input("Введите кол-во, которое Вам нужно: "))
if k <= n * m and (k % m == 0 or k % n == 0):
    print('yes')
else:
    print('no')