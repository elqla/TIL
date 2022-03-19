def solution(n, k):  # 양의정수 n , k진수로 바꿈

    lst =[]
    while n>=k:
        m = n//k #몫
        a = n%k #나머지
        lst.append(a)
        n = m
    lst.append(n)

    lst.split(0)



# p = 0을 포함하지 않는 수, 1과 자기자신을 약수로 가지는 수
# 소수의 개수 구하기


