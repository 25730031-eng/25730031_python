#1 range
a = input()

for i in range (len(a)):
    print (a[i], end =" ")

print()

#2 리스트
a = input()

for i in a:
    print(i, end =" ")

print()

#3join 사용 구분자.join (문자열 반복가능객체)
a = input()
print(" ".join(a))
