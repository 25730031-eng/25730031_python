a = [i for i in range(100)]
print(a)


b = [i for i in range(1, 101) if i % 2==0]#수식 for (변수 in 리스트) if (조건)
print(b)


squares = [ x*x for x in range(10) ]

squares = []
for x in range(10):
    squares.append(x*x)

numbers=[]

for x in range(100):
    if x%2 == 0 and x % 3 == 0:
        numbers.append(x)

print(numbers)
