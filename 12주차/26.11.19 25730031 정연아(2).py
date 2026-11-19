#문자열 인덱스
letters = 'python'
print(letters[0], letters[2])

string = "홀짝홀짝홀짝홀짝"
print(string[::2])
print(string[1::2])

#슬라이싱
license_plate = "24가 2210"
print(license_plate[-4::])

string = "PYTHON"
print(string[::-1])

#문자열.replace
#변경X
phone_number = "010-1111-2222"
print (phone_number.replace("-", " "))
print(phone_number)
#변경O
phone_number = "010-1111-2222"
print (phone_number.replace("-", ""))
phone_number = phone_number.replace("-", "")
print(phone_number)

print("-"*30)
#split()->결과를 리스트로 반환
url = "http://sharebook.kr"
url_split = url.split('.')
print(type(url.split('.')))


url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

print("-"*30)

#문자 + 문자 = 연결
a = "3"
b = "4"
print(a + b)

#문자*숫자 = 문자를 숫자만큼 반복해서 출력
a = "hi"
print (a*10)

t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
#print((t1, t2)*4)

상장주식수 = "5,969,782,550"
컴마제거 = int(상장주식수.replace(",", ""))

#strip -> 좌우 공백 제거
data = "   삼성전자    "
data1 = data.strip()
print(data1)


a = "hello world"
a.split()

ticker = "btc_krw"
ticker.split("_")

#49
date = "2025-05-01"
temp = date.split("-")

year=temp[0]
month=temp[1]
day=temp[2]

print(year)
print(month)
print(day)
