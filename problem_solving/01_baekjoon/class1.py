# #1152 단어의 개수

word = input().split()
print(len(word))


# #1157 단어 공부
words = input().upper()
word_list = list(set(words))

cnt_list=[]
for x in word_list:
    cnt = words.count(x)
    cnt_list.append(cnt)
    #cnt_list.append(words.count(x))
if cnt_list.count(max(cnt_list))>1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(word_list[max_index])
    #print(word_list[cnt_list.index(max(cnt_list))])



#1330 두 수 비교하기
a, b = map(int, input().split())
if a>b:
    print('>')
elif a<b:
    print('<')
else:
    print('==')



#1546 평균
n=int(input())
m=list(map(int, input().split()))
max_score=max(m)

sum_list=[]
for score in m:
    sum_list.append(score/max_score*100)
test = sum(sum_list)/n
print(test)


#2438 별찍기
n = int(input())
for i in range(1, n+1):
    print('*'*i)

#2439 별찍기
n = int(input())
for i in range(1, n+1):
    print(" "*(n-i) + "*"* i)


#2475 검증수
number = list(map(int, input().split()))

sumnum = 0
for num in number:
    sumnum += num**2

print(sumnum % 10)


#2562 최댓값
n_list=[]
for num in range(9):
    n_list.append(int(input()))
print(max(n_list))
print(n_list.index(max(n_list))+1)


#2577 숫자의 개수
a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))
for i in range(10):
    print(result.count(str(i)))


#2567 문자열 반복
#s를 *r => P print(p)
t = int(input())
for i in range(t):
    r, str = input().split()
    p = ''
    for s in str:
        p += s*int(r)
    print(p)



#2739 구구단
n = int(input())
for i in range(1, 10):
    print(n,'*', i, '=', n*i)


#2741 n찍기
for i in range(1, int(input())+1):
    print(i)

#2742 기찍N
n = int(input())
for i in range(n, 0, -1):
    print(i)

#2753 윤년
year = int(input())
print(1) if year%4==0 and year%100!=0 else print(1) if year%400==0 else print(0) 

#
year = int(input())
if ((year%4==0)and (year%100!=0) or (year%400 ==0)):
    print(1)
else:
    print(0)


#2884 알람시계
h, m = map(int, input().split())
#45분 앞서서
if m >= 45:
    print(h, m-45)
elif h==0 and m <45:
    print(23, m+15)
else:  #m<45 또는 h!=0
    print(h-1, m+15)




#2908 상수
#거꾸로 했을때 큰 수 출력하기
input_list = list(input().split())
result_list =[]
for number in input_list:
    result = ''
    for num in number:
        result = str(num) + result
    result_list.append(result)
print(max(result_list))

#
n, m = input().split()
n = int(n[::-1])
m = int(m[::-1])

if n > m:
    print(n)
if  m > n:
    print(m)

#
n, m = input().split()
n = int(n[::-1])
m = int(m[::-1])
print(n) if n >m else print(m)




#2920 음계
input_list = list(map(int, input().split()))
if input_list == sorted(input_list):
    print('ascending')
elif input_list == sorted(input_list, reverse=True):
    print('descending')
else:
    print('mixed')


#3052 나머지
lst = []
for i in range(10):
    n = int(input())
    lst.append(n%42)
lst = set(lst)
print(len(lst))



#8958 OX퀴즈
n = int(input())
for i in range(n):
    a = input()
    score = 0
    sumscore = 0
    for j in a:
        if j =='O':
            score+=1
        else:
            score = 0
        sumscore += score
    print(sumscore)



#10809 알파벳 찾기
word = input()
for a in range(97, 123):
    print(word.find(chr(a)), end=' ')


#
word = input()
abc ='abcdefghijklmnopqrstuvwxyz'
for a in abc:
    if a in word:
        print(word.find(a), end=' ')
    else:
        print(-1, end=' ')


#10818 최소, 최대
num = input()
num_list = list(map(int, input().split()))
print(min(num_list), max(num_list))

#
cnt = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
min = numbers[0]

for i in numbers[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i

print(min,max)


#10871 X보다 작은 수
a, x = list(map(int, input().split()))
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=" ")


#10950 A+B-3
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(a+b)


#10951 A+B-4
while True:
    try:
        a, b = map(int,input().split())
        print(a+b)
    except:
        break


#10952 A+B -5
import sys
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a ==0 and b==0:
        break
    else:
        print(a+b)



#11654 아스키코드 출력
#ord(문자) = 숫자
#chr(숫자) = 문자
ask = input()
print(ord(ask))




#11720 (연속된)숫자의 합
n = int(input())
print(sum(map(int, input())))


#
n = input()
num = input()
s = 0
for nu in num:
    s += int(nu)
print(s)


#
n = int(input())
num = input()
s = 0
for i in range(n):
    s+=int(num[i])
print(s)