'''
fruits = ["딸기", "수박", "복숭아", "자몽"]

color1 = ['빨강', '노랑']
color2 = ['초록', '파랑']
print(color1 + color2)  #['빨강', '노랑', '초록', '파랑']
# 문자열과 동일하게 동작

# 리스트 반복
print(color1*2)

# 리스트 길이
print(len(color1))  # 2

# 요소의 수정
color1[1]="하늘색"
print(color1)

 리스트는 순서대로 정리된 항목을 담고 있는 데이터, 인덱싱과 슬라이싱을 할 수 있다 '''




# sort 함수는 리스트 요소를 오름차순으로 정리한다
num = [1,5,6,2,3]
korean = ["강아지", "고양이", "멍멍이", "가나지"]
english = ["a","b","d","g"]

# sort 함수는 숫자는 크기순, 한글과 영어는 사전 순으로 정리한다

num.sort()
korean.sort()
english.sort()
print(num)
print(korean)
print(english)


# reverse 함수, 리스트 순서를 뒤집는 함수 (맨 뒤, 맨 앞 반대)
print("뒤집기 전", num)
num.reverse()
print("뒤집은 후", num)

