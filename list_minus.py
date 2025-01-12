# 리스트에서 요소 삭제하기
# pop(위치) : 해당 인덱스 번호의 요소를 삭제
# del키워드 : 인덱스 번호로 요소 삭제
# remove(요소) : 리스트에서 첫 번 째로 나오는 해당요소를 삭제
# clear() : 리스트의 모든 요소를 삭제, 빈 배열로 만듦

name = ["강", "박", "권", "김", "이"]

# pop(인덱스)
print("pop-리스트 요소 삭제")
print("전 :", name)
name.pop(0) # 인덱스 번호를 생략하면 자동으로 -1이 되어, 마지막 요소를 지운다
print("후: ", name)
print()

del name[2]
print(name)

del name[2:]
print(name)

# 여기서 del과 pop은 둘 다 인덱스 요소로 삭제를 하지만, 다른 점은 pop은 하나만 삭제할 수 있는데 del은 여러개의 인덱스를 삭제할 수 있다는 거임

# remove() : 리스트의 요소값 이용
name.remove("권")
print(name)
# remove 함수는 요소값이 리스트에 여러개 있는 경우 제일 앞에 있는 하나만 삭제

# clear함수는 요소값을 전부삭제
name.clear()
print(name)

