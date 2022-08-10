# 풀이1
N = 5  # 개의 자연수
M = 8
K = 3
# M번 더해서 큰수 만들기
# k번 까지 쓸 수 있음

lst = [2, 4, 5, 4, 6]
# 가장 큰 수 두개를 구해서 연속으로 더하기
mx = max(lst)
lst.remove(mx)
mx2 = max(lst)

res = 0
for i in range(M//K + 1):  # 0, 1, 2   111 222 33
    if i == M//K:
        K = M % K
    if i//2:
        res += mx2*K
    else:
        res += mx*K
print(res)


# 풀이2
lst.sort()
mx = lst[N-1]
mx2 = lst[N-2]

# 가장 큰 수가 더해지는 횟수 계산
