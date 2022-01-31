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
        print(f'저는 {self.name}학생입니다')  #부모클래스의 메소드를 실행시키고 싶을때

# p1 = Professor('김교수')
# p1.talk()
s1 = Student('다빈')
s1.talk()   #반갑습니다. 다빈입니다.  super().talk()
                #저는 다빈학생입니다
print("------------------------------")
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'반갑습니다. {self.name}입니다.')

class Professor(Person):
    def talk(self):
        print('{self.name}일세')

class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        print(f'저는 {self.name}학생입니다')

s1 = Student('다빈')        #저는 다빈학생입니다.      초기화 메소드 +print  라서?
s1.talk()                #반갑습니다. 다빈입니다.      인잇을 써주면서 위에꺼를 무시(초기화) 


#위는 인잇이 없고, 밑엔 인잇이 있음
#위는 talk호출 시 위 + 본인을 프린트하고, 아래는 위만 프린트함.
#               class Person+Student ,  class Person



print("=============================================================")


class Animal():
    
    def walk(self):
        print('걷는다.')
    def eat(self):
        print('먹는다.')
    def greet(self):
        print('인사한다.')

class Human(Animal):
    def wave(self):
        print('손을 흔들면서')

    def greet(self):     #자식클래스에서 (greet을) 오버라이드한 메소드에서 
        self.wave()
        super().greet()    #부모클래스의 메소드를 쓰고 싶을때는 super().메소드

h1 = Human()     #인잇이 없어서 뭐가 생성되진 않음?
h1.greet()       #손을 흔들면서\n인사한다.


print("------------")
#이렇게 주로 쓰임

class Animal():
    def __init__(self, name):
        self.name = name  
    def greet(self):
        print('{}이 인사한다.'.format(self.name))

class Human(Animal):

    def __init__(self, name, hand):
        super().__init__(name)   #name 처리 /C-Animal-init->greet
        self.hand = hand


    def wave(self):
        print('{}손을 흔들면서'.format(self.hand))
    def greet(self):     #자식클래스에서 (greet을) 오버라이드한 메소드에서 
        self.wave()
        super().greet()   


h1 = Human("사람", '오른')   #인잇에서 이름을 받아옴
h1.greet() 


print("------------")

class Animal():
    def __init__(self, name):
        self.name = name

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand

h1 = Human('지선', '손손')    #인잇에 네임이 들어가 있어서
print(h1.hand)       


print("------------")
class Car():
    
    def __init__(self, name):
        self.name = name
    
    def run(self):
        print("차가 달립니다.")

class Truck(Car):
    # 이 아래에서 __init__ 메소드를 오버라이드 하세요.
    def __init__(self, name, capacity):
        super().__init__(name)
        self.capacity = capacity
    def load(self):
        print("에 짐을 실었습니다.")
        
t1 = Truck("트럭", "공간")
print(t1.name)  #트럭
t1.load()       #에 짐을 실었습니다.
print("------------")

class Animal:
    def __init__(self, name):
        self.name = name
        print(f'동물이름은 {self.name}')
    def talk(self):
        print('으르렁')

class Person(Animal):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
    def talk(self):
        print('hi')

p1 = Person('다빈', '33')  #동물이름은 다빈  #위에껄 받아와서 프린트 했네...
p1.talk() #hi


#########super로 받아오지 않고, 위에꺼를 완전 재정의 시켜버리기 !

class Animal:
    def __init__(self, name):
        self.name = name
        print(f'동물이름은 {self.name}')
    def talk(self):
        print('으르렁')

class Person(Animal):
    def __init__(self, name, email):
        self.name =  name
        self.email = email
    def talk(self):
        super().talk()

p1 = Person('다빈', 12345)
p1.talk()


