#1 ', " 구분
print ('신씨가 소리질렸다"도둑이야"')

#2
print("Marry's cosmetic")

#3 print(sep=' ')
print(1, 2, 3, 4, 5, 6, sep='/')

#7
print("naver", "kakao", "sk", "samsung", sep=';')

#9
print("first", end=""); print("second")

#13
s = "hello"
t = "python"
print(s+"!", t)


print("-"*30)


#type
#int 정수
a = 128
print(type(a))
#str 문자
a="128"
print(type(a))
#float 실수
a=12.5
print(type(a))

print("-"*30)


#str -> int
#대입해서 변수를 int 변경
a = 128
b=int(a)
print (type(a))
a= int(a)

#변수에 데이터 타입을 변경하지 않고 사용
a="128"
print(type(int(a)))

#정수 -> 실수
b =123
b= float(b)
print(type(b))

#정수 -> 문자열
c =123
c = str(c)
print(type(c))

print("-"*30)
