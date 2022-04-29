# 직사각형
#x1, y1, x2, y2 = list(map(int, input().split()))

# 면적 구하기 X
# 면적을 갖는 곳에 1, 없으면 0
# 면적을 갖는 곳 count 혹은 가지면서 +1

'''
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
'''


arr = [[0]*100 for _ in range(100)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):  # x: 0~2 (차지하는칸 2칸)
        for y in range(y1, y2):
            if arr[x][y] == 0:
                arr[x][y] += 1
                cnt += 1

print(cnt)

#이중리스트라서 arr. count(1) 하면 값이 안나옴
#1
answer = []
for ele in arr:
    answer += ele
print(answer.count(1))

#2
answer = sum(arr, [])   #sum(iterable, start=0)   
                        # iterable의 합을 해줄 건데, 여기선 리스트를 더해주자...의 의미?
                    
print(answer.count(1))


#3
import itertools
answer = list(itertools.chain.from_iterable(arr))


#4
import itertools
answer = list(itertools.chain(*arr))

#5
answer = [element for a in arr for element in a]
        #ele먼트는 for a in arr
            #arr안의 a에(이중리스트 안의 리스트에 있음)
            #for element in a  #이중리스트 안 리스트의 요소구하기
            #element 는 a에 있어

#6
from functools import reduce   #누적합 구하는 함수
import operator
answer = list(reduce(lambda x, y: x+y, arr))  #람다, 리턴문이 필요 x


#7
print('----')
b = []
for a in arr:
    b.extend(a)  #append쓰면 리스트가 그대로 들어가서 extend로 요소만 넣어줌
print(b.count(1))








