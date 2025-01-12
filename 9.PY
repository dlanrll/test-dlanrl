# for문 : 프로그래머가 지정한 횟수만큼 반복
# while문 : 특정 조건을 만족하는 동안 계속 반복
'''
num = [0, 1, 2, 3, 4]

for i in num:
    print(i)

snack = ["홈런볼", "새우깡", "포카칩", "다이제"]

print('START')
for i in snack:
    print(i)
print("END")

# range() 함수 : "A에서 B사이다" 라는 의미를 가짐, 연속적 숫자를 만듬

a = range(10)

for i in a :
    print(i, end = "")
print()

a = range(10) 
b = range(1, 11)
c = range(3, 12, 2)

for i in a: # for i in range(10):   
    print(i, end= ' ') # 0 1 2 3 4 5 6 7 8 9
print()

for i in b: # for i in range(1, 11):
    print(i, end= ' ') # 1 2 3 4 5 6 7 8 9 10
print()

for i in c: # for i in range(3, 12, 2):
    print(i, end=' ')
print()
'''

a = range(10) 
b = range(1, 11)
c = range(3, 12, 2)

for i in a: # for i in range(10):   
    print(i, end= ' ') # 0 1 2 3 4 5 6 7 8 9
print()

for i in b: # for i in range(1, 11):
    print(i, end= ' ') # 1 2 3 4 5 6 7 8 9 10
print()

for i in c: # for i in range(3, 12, 2):
    print(i, end=' ')
print()