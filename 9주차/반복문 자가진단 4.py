n = int(input("숫자를 입력하세요: "))
total = 0

# for i in range 문법 활용
for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print(total)
