import os
def clearScreen(): # os에 특화된 팁.
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    
    os.system(command)

class SmartPhone:
    def __init__(self, phoneOwner=None, phoneNumber=None, company=None, addres = None):
        self.__phoneOwner= phoneOwner
        self.__phoneNumber=company
        self.__company=company
        self.__addres=addres
    def __str__(self):  
        str_res = (f"폰 주인 이름: {self.__phoneOwner}\n"
                   f"폰 번호: {self.__phoneNumber}\n"
                   f"통신사: {self.__company}\n"
                   f"폰 주인 주소: {self.__addres}")
        return str_res
    
    # 찾는 이름이 포함되어 있으면 True
    def isNameContain(self, name):
        if name in self.__phoneOwner or name in self.__phoneNumber or name in self.__company or name in self.__addres : 
            return True
        else:
            return False

    # 찾는 이름이 완벽하게 일치하면 True    
    def isNameExist(self, name):
        if self.__phoneOwner == name or self.__phoneNumber == name or self.__company == name or self.__addres == name:
            return True
        else:
            return False
        
    # 변수 값 가져오기 getter 함수
    def get_phoneOwner(self):
        return self.__phoneOwner
    
    def get_phoneNumber(self):
        return self.__phoneNumber
    
    def get_Company(self):
        return self.__company
    
    def get_addres(self):
        return self.__addres
    

def run():
    clearScreen()
    lst_phone = [] 
    load_phone(lst_phone)
    while True:
        sel_menu = set_menu()
        if sel_menu== 1:
            print("------------")
            try:

                phone = set_phone()
                lst_phone.append(phone)
                print("연락처 입력 성공!!")
            except Exception as e:
                print(f"연락처 입력 실패!! {e}")

        elif sel_menu == 2:
            print("------------")
            print("연락처 출력")
            print("------------")
            get_phone(lst_phone)

        elif sel_menu == 3:
            print("------------")
            print("연락처 검색")
            print("------------")
            pp = input("검색할 연락처 (이름, 번호, 통신사, 주소)   > ")
            search_phone(lst_phone, pp)
                    

        elif sel_menu == 4:
            print("------------")
            print("연락처 삭제")
            print("------------")
            qq = input("삭제할 연락처 입력 > ")
            del_phone(lst_phone, qq)

        elif sel_menu == 5:
            save_phone(lst_phone)
            break # 반복문 탈출.
        else:
            pass             
        input() # 입력대기 : 엔터치면 넘어감   
        clearScreen()     
def search_phone(items: list, pp: str):
    count = 0
    for item in items: 
        if item.isNameContain(pp): 
            count += 1 # 검색된 결과가 있음
            print(item)
            print("------------") #  구분자
    print(f"검색 데이터 수 : {count}개")
    

def del_phone(items: list, qq: str):
 
    for i, item in enumerate(items): # 인덱스번호 출력
        if item.isNameExist(qq):
            del items[i] # 인덱스로 리스트에 요소하나를 삭제
            print("연락처 삭제 성공!!")
        else:
            print("연락처 삭제 실패!!")

        


# 폴더에 파일로 연락처리스트 저장
def save_phone(items: list):
    f = open("phone_db.txt", encoding="utf-8", mode="w") # 파일쓰기로 오픈
    for item in items:
        f.write(f"{item.get_phoneOwner()}|")
        f.write(f"{item.get_phoneNumber()}|")
        f.write(f"{item.get_Company()}|")
        f.write(f"{item.get_addres()}\n")
    
    f.close()

def load_phone(items: list):
    f = open("phone_db.txt", encoding="utf-8", mode="r") # 파일쓰기로 오픈
    while True:
        line = f.readline().replace('\n', '') 
        if not line: break # 무한루프 빠져나가는 조건
        lines = line.split("|") # 구분자로 잘라서 네개의 요소의 리스트 생성
        phoneOwner = lines[0]
        phoneNumber = lines[1]
        company = lines[2]
        addres = lines[3]  

        phone = SmartPhone(phoneOwner, phoneNumber, company, addres)
        items.append(phone)

    f.close()    

def set_phone():
    phoneOwner, phoneNumber, company, addres = input("연락처 입력 [이름|번호|통신사|주소] > ").split("|") # 입력 중 발생하는 예외
    phone = SmartPhone(phoneOwner = phoneOwner, phoneNumber = phoneNumber, company=company, addres = addres) # 데이터형 예외
    return phone

def get_phone(items: list):   
    for item in items:
        print(item)  
        print("------------") 
    print(f"총 데이터수 : {len(items)}개")


def set_menu():
    str_menu = (f"--연락처-- \n"
                "1. 연락처 입력\n"
                "2. 연락처 출력\n"
                "3. 연락처 검색\n"
                "4. 연락처 삭제\n"
                "5. 앱 종료\n")
    print(str_menu)
    try:
        sel_menu = int(input("메뉴 번호 입력: "))  
    except Exception as e:
        sel_menu = 0
    return sel_menu


if __name__ == "__main__":
    run()

print("프로그램 종료")