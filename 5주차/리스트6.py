n = int(input())
lst = []

for i in range(n):
    temp = int(input())
    lst.append(temp)

print (int(sum(lst)/n))


total = 0
for i in lst:
    total += i

print(int(total/len(lst)))
