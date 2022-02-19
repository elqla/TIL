#OOP
#함수 호출 관련 bound 개념 ! 
#우선 함수 > 메소드 이다.
#함수는 def ~~이라면, 메소드는 class안의 def ~~라고 볼 수 있다.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age

p1 = Person('다빈', 98)
print(p1.get_age)     #<bound method Person.get_age of <__main__.Person object at 0x00000296786BBD30>>
print(p1.get_age())   #98  

#class가 가지는 여러 멤버함수들은, self를 첫번째 입력인자로 가진다.
#이는 이 함수가 어떤 클래스에 속해있는 method라는 의미이며
#이를 bound method라고 한다.

#따라서 함수 호출 연산자 ()에 의해 호출되지 않은 메서드를 바운드 메서드(bound method)라 한다. 
#즉 바운드 메서드 = 호출되지 않은것.
#호출 없이 사용할땐 그냥 접근하였다 정도로 생각


class Person:
    def talk(self):
        print('말말말')
    def eat():
        print('잇잇잇')

p1 = Person()
p1.talk          #출력 안됨 #바운드메서드 #호출안된 메서드
print(p1.talk)   #<bound method Person.talk of <__main__.Person object at 0x000001851B399FD0>>
p1.talk()        #말말말

#p1.eat()        #TypeError: eat() takes 0 positional arguments but 1 was given
                #input값을 가지지 않는 메서드는 unbound method라고 한다.

##의문점 : init으로 정의된 것은 호출하지 않아도 되는건가? 
class Person:
    def __init__(self):
        print("생성")
p1 = Person()      #생성자 메소드 : 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드 !
                                #인스턴스 변수들의 초기값을 설정


class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')

p1 = Person("다빈")    #여기에서 일단 생성자를 호출함 ! p1 = Person()     
print(p1.name)   #다빈  ############ name 은 속성이니까 호출없이 나온다 ############
p1.talk()        #안녕, 나는 다빈 ### 함수 ####


#의문점 2
class Person:
    def __init__(self, age):
        self._age = age

    @property    #속성으로 가져오는 역할
    def age(self):
        return self._age

p1 = Person(10)
#print(p1.age())  #메서드(함수)라서 호출해야 하는데 
print(p1.age)     #데코레이터 때매 더이상 메서드를 의미하는게 아님
                 #메서드를 정의했는데, 실제론 속성처럼 쓰인다.

print("OOP시작====================================================================")


# 인스턴스 메소드/ 메소드 호출/ 인스턴스 조작
class Person:
    def talk(self):
        print('안녕')
    
    def eat(self, food):
        print(f'냠냠 {food}')

p1 = Person()
p1.eat('갈비')   #냠냠 갈비

print("=======================")
#생성자 메소드
class Person:
    def __init__(self, name):   #생성자 메소드 ! 
        self.name = name
    
    def talk(self):
        print(f'I am {self.name}')

p1 = Person('다빈')   #인자로 넘김
print(p1.name)        #다빈
p1.talk()             #I am 다빈

print("=======================")
#소멸자 메소드
# 소멸자 정의
def __del__(self):
    print('소멸될 때 자동으로 호출되는 메서드입니다.')
#소멸자 활용
#del 인스턴스
class Person:
    def __init__(self):
        print('응애')
    def __del__(self):
        print('으악')
p1 = Person()
del p1       

print("=======================")
#속성..
class Person:
    def __init__(self, name):
        self.name = name
        
    def talk(self):
        print(f'안녕, 나는 {self.name}')

p1 = Person("다빈")
print(p1.name)
p1.talk()

p1 = Person("이름바꿈")
p1.talk()

#p1 = Person()     #생성자 메소드도 함수라서, 인자의 개수가 안맞으면 에러남



print("=======================")
#class PascalCase:     클래스.변수명으로 접근
#         statement


class Circle:
    pi = 3.14     #클래스 영역에 정의된 것.

print(Circle.pi)

c1 = Circle()
c1.pi = 3.141592
print(c1.pi)

print("------")
class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

    def area(self):
        return Circle.pi*self.r*self.r

print(Circle.pi)

c1 = Circle(2)
print(c1.area())



print("=======================")
#클래스 메소드
#인스턴스와 구분되어, 클래스를 의미하는 cls(로직) 매개변수를 통해 클래스를 조작
'''
class MyClass:
    @classmethod
    def class_method(cls, arg1, arg2):  ##self처럼 cls전달
        return cls

# 자동으로 첫 번째 인자로 클래스(MyClass)가 들어갑니다.
print(MyClass.class_method())
'''
class MyClass:
    
    @classmethod  #클래스가 사용할 메소드
    def class_method(cls):
        return cls

print(MyClass.class_method())  #<class '__main__.MyClass'>
print(MyClass)                 #<class '__main__.MyClass'>
#위와 아래 호출 시 같은값을 가짐


class MyClass:
    var = 'Class 변수'
    
    @classmethod  #클래스가 사용할 메소드
    def class_method(cls):
        print(cls.var)
        return cls

MyClass.class_method()  #Class 변수
print(MyClass)  #<class '__main__.MyClass'>


print("=======================")
#스태틱 매소드
#클래스가 사용할 매소드. //  인스턴스&클래스의 속성과 무관 //
###호출시 어떠한 인자도 전달되지 않음### Utility 작동??
#클래스 정보에 접근/수정 불가

#1
class MyClass:
    
    @staticmethod
    def static_method(static):
        return static

print(MyClass.static_method('값 넘겨주자..'))
# static_method() missing 1 required positional argument: 'static'
##함수는 인풋값을 꼭 넣어줘야 함

#2
class MyClass:

    @staticmethod
    def static_method(): 
        return 'static'

print(MyClass.static_method())

#3
class MathUtility:
    
    @staticmethod
    def get_e():
        return 2
print(MathUtility.get_e())

#4
class PersonUtility:
    
    @staticmethod
    def get_phone_number(phone_number):
        return phone_number[:2] + ')'+phone_number[2:]

print(PersonUtility.get_phone_number('0215775588'))

print("=======================")
class MyClass:

    # 함수는 기본적으로 로컬 스코프 
    # 내부에서 활용하고 싶으면 파라미터로 받도록 정의!
    
    # 인스턴스 메서드 : 인스턴스를 조작하고 싶어
    # (파이썬제작자) 함수 내부에 인스턴스를 던져주도록 설계
    # 메서드를 정의할 때 self로 받도록 
    # 클래스 상태를 수정할 수도 있음
    def instance_method(self):
        return self 
    
    # 클래스 메서드 : 클래스를 조작하고 싶어
    # (파이썬제작자) 함수 내부에 클래스를 던져주도록 설계 
    # 메서드를 정의할 때 cls로 받도록
    # 객체 인스턴스 상태를 수정할 수 없음
    @classmethod
    def class_method(cls):
        print(cls.var)
        return cls
    
    # 스태틱 메서드 : 클래스나 인스턴스를 조작할 생각은 없는데 함수를 쓸거야
    # self, 매개변수 사용 XXXX 
    # 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    @staticmethod
    def static_method():
        return ''





print("=======================")
#인스턴스와 클래스간의 이름공간 (namespace)

class Person:
    species = 'human'
    
    def __init__(self, name):       #클래스 이름공간
        self.name = name 
        
p1 = Person('Hong')              #인스턴스별 이름공간
p2 = Person('Choi')
print(p1.name)
print(p2.name)



class Person:
    name = 'unknown'
    def talk(self):
        print(self.name)
p1 = Person()
p1.talk()   #unknown  인스턴스 변수 정의되있지 않아서


p2 = Person()
p2.talk()      #unknown
p2.name='kim'
p2.talk()      #kim


print(Person.name)  #unknown
print(p1.name)
print(p2.name) #kim





print("=======================")
#메서드 추가
#매직/스폐셜 메서드 (더블언더스코어(__)가 있는 메서드)
'dir('')'
'''__str__(self):       유저 친화적(formalX)

    class Person:
    def __str__(self):
        return '객체 출력(print)시 보여줄 내용'

    #특정 객체를 출력(print()) 할 때 보여줄 내용을 정의할 수 있습니다.
'''
'__len__(self)'
'__repr__(self)           formal O -Developer'
'__lt__(self, other)'
'__le__(self, other)'
'__eq__(self, other)    print(p1 == p2)  '
'__ne__(self, other)'
'__gt__(self, other)'
'__ge__(self, other)'

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'나는 {self.name}'

p1 = Person('다빈')
print(str(p1))



class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __gt__(self, other):
        print(f'{self.name}: {self.age}살 / {other.name}: {other.age}살')
        return self.age > other.age

p1 = Person('재영', 100, 190)
p2 = Person('지선', 10, 185)
print(p1 > p2)



print("===========OOP핵심개념================")
#추상화
#세부적이지 X < 필수적인 부분만 표현

class Person:
    pass
class Student(Person):
    pass
class Professor(Person):
    pass


#상속
#부모클래스 -> 자식클래스  : 코드재사용성 증가

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다, {self.name}입니다.')
p1 = Person('다빈', 25)
p1. talk()

class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department  # 또 안쓰려면 밑에 SUPER
prof1 = Professor('김교수', 40, '컴공')

print(prof1.name)
prof1.talk()

print("-------")

'''
issubclass(class, calssinfo) class가 classinfo의 subclass인 경우 True
issubclass(Student,Person) = True
           bool, int = True
           float, int = False

isinstance(object, classinfo)
           object classinfo의 인스턴스거나
           subclass인 경우 => True
           △다른 하위 클래스랑 불일치시 Fasle
isinstance(s1, Student) = True
isinstance(s1, Person) = True
'''



print("-------")
#super
#자식이 부모클래스를 사용하려고 할때!
#


class Person:
    def __init__(self, name, age):
        print('Person호출')
        self.name = name
        self.age = age

    def talk(self):
        print(f'반갑습니다. {self.name}입니다 ^^7')

class Student(Person):
    def __init__(self, name, age, student_id): #부모값 다갖고옴
        super().__init__(name, age)
        self.student_id = student_id



s1 = Student('다빈', 25, '2022')
print(s1.name)
print(s1.student_id)


print("--------------------------")

#상속, 클래스 메서드
class Person:
    population = 0

    @staticmethod
    def add_population():
        Person.population +=1
class Student(Person):
    population = 0

Person.add_population()
print(Person.population)  #1, 2, 3.,,,

Student.add_population()
print(Student.population)   #0


print("--------------------------")

class Person:
    population = 0

    @classmethod
    def add_population(cls):
        cls.population += 1
class Student(Person):
    population = 0    

Person.add_population()
print(Person.population)      #1, 2, 3 ,...

Student.add_population()
print(Student.population)    #1, 2, 3 ,...


print("--------------------------")
#메소드 오버라이딩/ 무시하다, 우선하다.
#상속받은 메소드 재정의/ 특정기능 변경
#상속 받은 클래스에서 #####같은 이름의 메서드로 덮어씁니다#####
# .__init__, __str__의 메서드를 정의
# class A:
#     name = 'A'
# class B(A):
#     name = 'B'
# class C(A):
#     name = 'C'
# class D(B, C):


class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def talk(self):
        print(f'{self.name}일세')  #덮어쓰기

class Student(Person):
    def talk(self):
        super().talk()
        print(f'저는 학생입니다')  #부모클래스의 메소드를 실행시키고 싶을때

p1 = Professor('김교수')
p1.talk()
s1 = Student('다빈')
s1.talk()       #반갑습니다. 다빈입니다.  super().talk()
                #저는 학생입니다


class Animal:
    def __init__(self, name):
        self.name = name
        print(f'동물이름은 {self.name}')
    def talk(self):
        print('으르렁')

class Person(Animal):
    def __init__(self, name, email):        #super로 위에 값을 받아오지 않고 인잇으로 오버라이딩 !
        self.name = name
        self.email = email
    def talk(self):
        print('안녕')

p1 = Person('다빈', '33')
p1.talk()
        
print("--------------------------")

#캡슐화/ 외부로부터의 직접적인 액세스를 차단
#다른 언어와 달리 파이썬에서 캡슐화는 암묵적으로는 존재하지만, 언어적으로는 존재하지 않습니다.

#Public Access Modifier
#일반적으로 작성되는 메소드와 속성
#어디서나 호출 가능, 오버라이드 허용

#1 캡슐화에선 이렇게 하는걸 원하지 않음 ! 변수에 직접접근 X
class Person:
    pass

p1 = Person()
p1.name = '다빈'
print(p1.name)


#2  이렇게 주로 사용함. (편의상 인잇 생략했음)
class Person():
    def get_name(self): 
        return self.name 
    def set_name(self, name):
        self.name = name    #순서 다르게 써도 상관없음. 겟으로 가져온다 ! 이런식으로 개념잡기
p1 = Person()
p1.set_name('셋네임')  #셋으로 정의하고
print(p1.get_name())   #겟으로 가져오기


#Protected Access Modifier
#언더바 1개로 시작하는 메소드나 속성
#상속관계에서 호출 가능
#하위 클래스에서 메서드 오버라이딩을 허용합니다.
#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age   #_를 써줌  #나이를 숨기고 싶다.

    def get_age(self):   #age는 직접접근하지 말자
        return self._age #한단계를 더 씌워놓는다.
p1 = Person('다빈', 25)
print(p1._age)  #이렇게 호출할 수도 있지만, 이 속성을 보자마자 알수 있음.
                #이러케 쓰지 말자.. 는 암묵적인..
print(p1.get_age())  #이렇게 쓰기

#Private Access Modifier
#본 클래스 내부에서만 사용가능
#접근 불가능(상속, 호출  등)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
p1 = Person('지선', 35)
#print(p1.__age)     #접근 불가능 !Person' object has no attribute '__age'
print(p1.get_age()) #를해서 봐야됨
#print(dir(p1))





print("-----------------------------")
#getter, setter Method
# 변수에 접근할 수 있는 메서드를 별도로 생성할 수 있습니다.

# getter 메서드: 변수의 값을 읽는 메서드입니다.
# @property 데코레이터를 사용합니다.

# setter 메서드: 변수의 값을 설정하는 성격의 메서드입니다.
# @변수.setter를 사용합니다.
class Person:
    def __init__(self, age):
        self._age = age
    @property    #속성으로 가져오는 역할
    def age(self):
        return self._age
    


p1 = Person(10)
#print(p1.age())  #함수, 메서드니까 호출하면,,오류뜸
print(p1.age)     #데코레이터 때매 더이상 메서드를 의미하는게 아님
                 #메서드를 정의했는데, 실제론 속성처럼 쓰인다.

class Person:
    def __init__(self, age):
        self._age = age
    @property    #속성으로 가져오는(get) 역할
    def age(self):
        return self._age
    
    @age.setter   #age에 setter를 지정
    def age(self, new_age):
        self._age  = new_age - 10


p1 = Person(56) 
print(p1.age)    #왜 이거 안되지ㅠㅠ

p1.age = 30
print(p1.age)   


print('----------')
#다중상속
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'xx'
    def swim(self):
        return '엄마 수영'

class Dad(Person):
    gene = 'xy'
    def walk(self):
        return '아빠 걸어'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째응애'

baby1=FirstChild('첫째')

print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene)



print('----------')
#상속관계에서의 이름공간과 MRO
#인스턴스 -> 클래스 순으로 나가는 과정에서 상속이 있으면
#인스턴스 ->자식클래스 -> 부모클래스
#MRO는 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 속성 또는 메서드


class Mom:
    def walk(self):
        print('사뿐사뿐')
        
        
class Dad:
    def walk(self):
        print('저벅저벅')

class Daughter(Mom, Dad):
    pass


class Son(Dad, Mom):
    pass


d = Daughter()
s = Son()

d.walk()
s.walk()


print(Daughter.__mro__) #(<class '__main__.Daughter'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class 'object'>)
print(Son.__mro__) #(<class '__main__.Son'>, <class '__main__.Dad'>, <class '__main__.Mom'>, <class 'object'>)