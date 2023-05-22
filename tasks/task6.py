#Task 6
n = int(input("Введите номер билета: "))
n1 = n // 100000
n2 = (n // 10000) % 10
n3 = (n // 1000) % 10
n4 = (n % 1000) // 100
n5 = (n % 100) // 10
n6 = n % 10
if n1 + n2 + n3 == n4 + n5 + n6:
    print('yes')
else:
    print('no')