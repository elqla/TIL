N = int(input())
arr = list(map(int, input().split()))
#중간에 위치한 값 구하기
#N=9 (idx 4 = 9//2)  ~199
mid_i = N//2
#카운팅정렬
#count
c = [0]*(N+1)
for i in range(N):
    c[arr[i]] +=1
#누적
for i in range(1, N):
    c[i] += c[i-1]

#new_arr
new_arr = [0]*N
for i in range(N-1, -1, -1):
    c[arr[i]] -= 1
    new_arr[c[arr[i]]] = arr[i]


#res
res = new_arr[N//2]
print(res)

