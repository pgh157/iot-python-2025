# for 문: 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#      구문안으로...

# 아래와 같이 출력되는 프로그램을 작성하시오.
'''
*
**
***
****
'''
# range() 범위를 생성 클래스
# 마지막 수 : max - 1
# range(8) -> range( 0, 8 )
# range(init, max, add)
# print(range(8))

# # for i in [0,1,2,3,4,5,6,7]: # 이 조건이 참인동안 반복...
# for i in range(0,8):
#     print(i)
# for i in range(0,8,2): # 짝수만

# num = int(input("최대별수 :  "))
# for i in range(1,num+1):
#     print("*"*i)

# 구구단
# 2단부터 2x9 ~ 9x9
# 2 x 1 = 2, 2 x 2 = 4
# for x in range(2,10):
#     for y in range(1,10):
#         print(f"{x} X {y} = {x*y}")



# 요구사항 - 한줄에 각 단씩 나오도록
# for x in range(2,10):
#     for y in range(1,10):
#         print(f"{x} X {y} = {x*y}", end=" ")
#     print() # 그냥 한줄 내리기

# print("구구단종료\n\n\n")
# 요구사항2 - x*y 값이 항상 두 줄씩 표현되도록
# for x in range(2,10):
#     for y in range(1,10):
#         print(f"{x} X {y} = {x*y:2d}", end="  ")
#     print() # 그냥 한줄 내리기

# print("구구단종료\n\n\n")

# 단 시작을 표시
# for x in range(2,10):
#     print(f"{x}단 시작")
#     for y in range(1,10):
#         print(f"{x} X {y} = {x*y:2d}", end="  ")
#     print() # 그냥 한줄 내리기

# 반복문 빠져나올 때 : break (자기 for 문에만 영향)
## 반복문에서 특정 조건을 지나칠때 : continue

for x in range(2,10):
    if x%2 ==1: continue
    # if x == 8: break
    print(f"{x}단 시작")
    for y in range(1,10):
        print(f"{x} X {y} = {x*y:2d}", end="  ")
    print() # 그냥 한줄 내리기