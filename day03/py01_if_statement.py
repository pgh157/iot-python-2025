# if 문 : 흐름제어 가장 기본
# 흐름제어문 마지막엔 항상 콜론(:)을 사용해야 함!
# if (참이되는 조건):     :(colon), ;(semi-colon)
#   if문 안으로 들어간다!

age = int(input("나이를 입력하세요."))

# 만약에 나이가 19세가 아니면 담배를 살 수 없음.
# 조건이 여러 개 일때 and, or로 계속 작성
# if age > 19 or age == 19: # 참인 조건, if 무조건 참
if age >=19 :
    print("4,500원 입니다.")
else: # False
    print("Bye")

grade = input("학점을 입력하시오(A | B | C | D | F)").upper() # 소문자도 대문자로 변경
if grade == 'A' or grade =='B': # 학점이 A이거나 B면, 이 구문에 걸리면
    # 구문안으로 들어간다.
    print("공부 열심히 하셨네요.")
    print("축하!!")
    if grade == 'A':
        print("장학금을 드리죠!")
    else:
        print("장학금까지 바랬냐??")

elif grade == 'C': # 학점이 C이면
    print("그럭저럭 하셨네요.")
else:
    print("공부 좀 해라!")

