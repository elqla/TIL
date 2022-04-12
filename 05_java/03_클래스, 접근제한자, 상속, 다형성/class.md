# class

[생성자](# 생성자)

- 배열 = 같은 타입 데이터의 모임
- 클래스
  - 객체를 생성하는 틀 ( 변수, 함수 ) 

- 객체

  - 속성- 멤버변수

  - 동작- 메소드

    ```java
    class TV{
        int channel;
        int vloumm; // 멤버변수
    //----------------------------
        public void channelup(){        
        }
        public void channeldown(){
        }//멤버함수, 메소드
    }
    TV tv = new TV();
    tv.channeldown();
    ```

- 클래스와 선언

```java
//Person.java _ class // class = 묶음 도장  (person class공간 안에 여러 데이터 존재)
public class Person {
	String name;
	int age;
	int height;
	void print()  {
		System.out.println("사람의 이름은 " + name + "입니다.");
		System.out.println("사람의 나이는 " + age + "입니다.");
		System.out.println("사람의 키는 " + height + "입니다.");
	}// 함수 내에서 name, age, height을 출력 ! 
}
```

```java
//persontest
.java _ class
int [] arr = new int[3];

Person p1 = new Person(); // p라는것이 name, age, height 위치 참조
p1.name = "Hong";
p1.age = 23;
p1.height = 179;   

p1.print(); //person_class에서 가져옴
System.out.println("사람의 이름은 " + p1.name + "입니다.");
```

```java
static void printPerson(Person p)  {
		System.out.println("사람의 이름은 " + p.name + "입니다.");
		System.out.println("사람의 나이는 " + p.age + "입니다.");
		System.out.println("사람의 키는 " + p.height + "입니다.");
	}
printPerson(p1);
```

- 함수

```java
public class FunctionTest {
	public static void main(String[] args) {
		System.out.println("Hellow world");
		work("자동차");
		System.out.println("집에가");
		work("자전거");
	}
	static void work(String name) {
		//string name = "자동차";
		System.out.println(name + "타고 출근");
		System.out.println("일한다.");
		System.out.println(name + "를 타고 퇴근");
	}
	//void = 반환할 값이 없다. (반환유형)
}
```





```java
public class Person {
	Person(String n, int a, int h){
		System.out.println("나 불렀니");
		name = n;
		age = a;
		height = h;
	}
    // 메소드 오버로딩: 이름이 같고 매개변수가 다른 함수를 여러개 정의하는 것
	void print(int n) {
		System.out.println("매개변수 정수 n");
	}
	void print(double n) {
		System.out.println("매개변수 실수 n");
	}
```

```java
		Person p1 = new Person("hong", 23, 153);   //생성자 호출
```



- 함수도 오버로딩이 가능하다.

  `class person`

```java
	// 메소드 오버로딩: 이름이 같고 매개변수가 다른 함수를 여러개 정의하는 것
	// 생성자도 함수니까, 오버로딩이 가능 ! 
	Person(String n, int a, int h){
		System.out.println("나 불렀니");
		name = n;
		age = a;
		height = h;
	}
	
	Person(){  //매개변수가 없을때
		System.out.println("기본 생성자");
	}
```





## 생성자

- 객체가 실행될때, 처음 한번 실행되는 함수
  - 객체의 초기화를 담당

- 클래스 명과 이름이 동일 

  ```java
  public class Dog{
      Dog(){
          sysout...
      }
  }
  ```

- 반환타입 X    ~~void도 xx~~
- 디폴트 생성자   `class dog{  }`
- `클래스명 ()`
- 오버로딩 지원
- 생성자를 만들지 않으면, 몸통이 비어있는 기본 생성자를 컴파일러가 자동으로 생성해줌 !



- this 의 활용

  - 현재 내가 동작하는 객체의 주소를 참조

  `class person`

  ```java
  void print()  {
  		int age = 10;
  		System.out.println("사람의 이름은 " + name + "입니다.");
  		System.out.println("사람의 나이는 " + this.age + "입니다."); 
  		// int age = 10이 가까울지라도, this를 쓰면 생성자에게 가까운 age 호출)
  ```

  ```java
  	Person(String name, int age, int height){
  		System.out.println("나 불렀니");
  		this.name = name;
  		this.age = age;
  		this.height = height;  //지역변수 이름이 멤버변수와 같을때, 멤버변수를 지목해줌
  	}// 모든 객체가 생성될때 수행되어야 하는 코드
  	Person(){ //다른 생성자를 호출할때는 이름 대신 this 키워드를 쓰도록 하고
                // this가 호출되는건 첫번째 행이어야 한다.
  		this("hong", 23, 156);
  ```

  

