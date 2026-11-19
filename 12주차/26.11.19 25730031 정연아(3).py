#append -> 맨 뒤에 원소 추가
movies = ["닥터 스트레인지", "스플릿", "럭키"]
movies.append("배트맨")
print(movies)

#insert -> 특정 위치에 값을 끼어넣기.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

#삭제 -> remove, del 리스트이름[인덱스] / pop[인덱스]
movies.remove("럭키")
#del movies[4]
#pop[4]

#56
a=['a', 'b', 'c']
b=['a', 'b', 'c']
c = a+b
print(c)

#57 max(), min()
a_list=[1,2,3,4,5,6,7,8]
print(max(a_list))
print(min(a_list))

#58 요소값 합
print(sum(a_list))

#59 요소의 개수
print(len(a_list))

#평균 (sum/len)
print(sum(a_list)/len(a_list))
