# 연산자

# 사칙연산 : + - * / 
a, b = 15, 14
# Shift + Delete 는 한줄 삭제 (매우 효율!)
print(a + b)
print(a - b)
print(a * b)

# 나누기 연산자 : /, //, %
a=14
b=4
print(a/b)  # 나눈 결과는 float
print(a//b) # 나눈 몫, int
print(a%b) # 나머지, int

# 거듭제곱(Power)
print(2**2)

# 연산자 우선순위
## 계산식이 복잡해서 연산자 우선순위를 잘모르겠으면 () 사용용
print((3 + 4 ) * 7)
print( 3 + ( 4 * 7 ) )

## 리스트 연산
## last index = len(list) - 1
listsample = [1, 3, 5, 7, 9]
print(listsample[0])
print(len(listsample)) # 리스트의 길이

print(listsample[1])
print(listsample[2])
print(listsample[3])
print(listsample[4])
listsample[4] = 11
print(listsample[len(listsample)-1])

## 문자열 연산 : +, * 만 존재
greeting = 'Hello'
target = 'World'
print(greeting , target) # 문자열 연산 x

print(greeting + " " + target) # 문자열 연산 + string concatenate (문자열 연결)
print(f'{greeting} { target}')
print('{0} {1}'.format(greeting, target))

print(greeting * 5 ) # 해당문자열을 * 수로 반복

## 문자열( Charactor Array) : List와 유사하지만 값 수정 불가
print(greeting[1])  # 리스트 연산
# greeting[0] =  'C'
print(greeting)

## 리스트 연산, 슬라이싱
listSample = ['2', '0', '2', '5', '-', '0', '2', '-', '0', '4']
current = '2025-02-04'

for i in listSample:
    print(i, end= '')
print()

print(current)
# 준비 끝

# 인덱싱, 인덱스에 있는 값을 가져오기
print(listSample[-1])
print(current[-1])

# 슬라이싱, 리스트를 자르기
## [start:end] : end - 1 까지만 추출
print(listSample[0:3 + 1])
print(current[0:3 + 1])

# 2025-02-04
year = current[0:3 + 1]
month = current[5:6 + 1] 
day = current[8: ] # end 끝까지는 숫자 생략
print(year, month, day)
print(current[-2: ])

## 문자열 연산 중 함수를 사용
full_name = "Hugo MH. Sung"
# 자르기
print(full_name.split())
print(full_name.split(' '))

names = full_name.split(' ')
print(type(names))
print(names)

names = full_name.split('.')
print(type(names))
print(names)

# 바꾸기
print(full_name.replace('Hugo MH.', 'Ashley'))

# 공백제거
origin='     Hello ~     '
print(f'//{origin}//')
print(f'//{origin.lstrip()}//')
print(f'//{origin.rstrip()}//')
print(f'//{origin.strip()}//') # 문자들 사이에 공백은 제거x

# 단어찾기
full_name = "Hugo MG. Sung"
print(full_name.find('G'))
print(full_name.find('h')) # -1 : h를 찾을 수 없음!

print(full_name.count('g')) # g가 문장에 몇번 존재
# print(full_name.index('h')) # 오류 발생! (find위주로 사용하기)

print(full_name.upper()) 
print(full_name.lower()) 

## T로 자를 때
# '', "" == empty(비어있다)
# ' '. " " == Space(공백존재)
origin = 'ITESTSTRING'
print(origin.split('T'))
