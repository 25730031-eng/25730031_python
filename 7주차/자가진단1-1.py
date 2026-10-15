#슬라이싱

a = input()
print(*a[::2])

#enumerate

s = input()

for i, c in enumerate(s):
    if i % 2 == 0:
        print(c, end=" ")


c = input()
for i in range(len(n)):
    if i %2 == 0:
        print(c[i], end=" ")
