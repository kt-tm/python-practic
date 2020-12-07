n = input("Введите число ")
n = int(n)
mx = 0
if n == 0:
    print(0)
while n > 0:
    if n % 10 > mx:
        mx = n % 10
    n = n // 10
print(mx)


