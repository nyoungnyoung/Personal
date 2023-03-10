# 1. 클래스 작성법
# class 클래스 이름 : 클래스이름 >> 대문자로 시작(단어가 바뀌면 다시 대문자로)

class Student:
    # 클래스 변수 : 인스턴스마다 별도로 가지는 데이터가 아니라
    # 공통으로 가지는 데이터의 경우에 클래스 변수로 선언함
    count_student = 0

    def __init__(self, name, age, score):         # init 메서드 : 생성자(Constructor)
        # 위 괄호에 들어가있는 name, age, score는 매개변수
        # 생성자 안에, 생성하려는 속성을 작성
        # '.' operator >>> 대상.속성  :  대상의 속성을 가져와라....
        # 앞으로 calss 내에서 self는 만들어진 인스턴스를 칭한다고 생각하면 됨!
        self.age = age          # 받아온 age라는 매개변수를 age라는 인스턴스에 집어넣겠다!
        self.name = name
        self.socre = score
        Student.plus_student_cnt()
        # self.count_student = 0
        # Student.count_student += 1
    
    def say_hello(self):
        print(f'안녕하세요 저는 {self.age}살 {self.name} 입니다.')
        # 인스턴스 메서드 내에서 클래스 변수 접근
        print(Student.count_student)

    @classmethod                    # 얘가 있으면 클래스 메서드
    def plus_student_cnt(cls):
        Student.count_student += 1

# 2. 객체(인스턴스) 생성
# 클래스이름() : 객체 생성됨 >>> 생성자 호출

s1 = Student('홍길동',17,66)  # Student()로 객체 생성 & 객체 주소값을 s1 변수에 할당
# s1은 변수이지만 Student 클래스의 인스턴스를 지칭하기 때문에, s1을 인스턴스라고 표현
# s1은 Student 클래스에 선언한 특징(속성 및 메서드)를 가지고 있음
# s1. << '.' operator 사용하면 s1의 속성값 및 메서드 사용가능
# 학생들의 속성(이름, 나이, 점수)를 넣어보자. 
# 실제 세계에서 학생들은... 전부 다른 나이, 이름, 점수를 가진다.
# >>>>>> 인스턴스마다 다른 값을 가짐!! >>>>>> 이런 특징을 가지는 값을
# '인스턴스 변수'라는 곳에 저장해보자
# '인스턴스 변수'는 어떻게 만드나요?
print(s1.age,s1.name,s1.socre)

s2 = Student('김싸피',20,100)
s3 = Student('이싸피',25,100)
s4 = Student('박싸피',26,100)
s5 = Student('최싸피',27,100)
s6 = Student('윤싸피',28,100)

# 학생관리 프로그램 같은거 만들때도 활용 가능할듯!

################ 클래스 변수 #################
# 클래스 변수는 인스턴스랑은 상관없다. 인스턴스가 있던 말던 사용가능
# 그래서 사실은 인스턴스를 통해(s1.count_student = 100) 형태로
# 접근은 가능하지만, 이렇게 쓰면 안된다!!
# 웬만하면 클래스 접근 방식(Student.count_student)으로 사용하기

########################################################
# 메서드 : 클래스 내부의 데이터를 활용해서 동작하는 함수
# 인스턴스 메서드 : 인스턴스 변수를 활용
# 클래스 메서드 : 클래스 변수를 활용
# 스태틱 메서드 : 인스턴스, 클래스 변수를 활용하지 않는 함수
# 메서드 선언 방법

# 클래스 내에서 인스턴스 변수/메서드를 사용하기 위해서는
# 항상 self.'뭐시기[()]' 형태로 사용한다!
s1.say_hello()

