n = int(input("입력 받을 값"))

print (n, end =" ")

for i in range (n):
    n = n // 2
    print (n, end = " ")

    if n <= 1:
        break
