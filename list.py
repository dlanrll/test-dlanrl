num = [1,5,6,2,3]
korean = ["강아지", "고양이", "멍멍이", "가나지"]
english = ["a","b","d","g"]

# 리스트 추가하기
print("맨 뒤에 요소 추가하기 :")
num.append(4)
print(num)

# insert 함수, 리스트 중간에 요소를 삽입할 수 있음
korean.insert(0, "냥냥이") # insert(인덱스 위치, 추가할 내용)
print(korean)

# 리스트 추가 관련 함수
# 한 번에 하나의 요소를 추가하는 함수 append(요소), insert(위치, 요소)
# 리스트에 리스트를 추가하는 함수 extend(리스트)

english.extend(["i am a girl", "meow"])
print(english)