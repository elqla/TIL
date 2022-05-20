from itertools import permutations
import sys
input = sys.stdin.readline


N = int(input())
num = list(map(int, input().split()))

k = ['+', '-', 'x', '/']
v = list(map(int, input().split()))
dic = []
for i in range(4):
    dic.extend(list(k[i]*v[i]))



perms = set(permutations(dic, N-1))

mx = -1000000001
mn = 1000000001
for perm in perms:
    s = num[0]
    for i in range(1, N):
        operator = perm[i-1]
        target = num[i]
        if operator=='+':
            s += target
        elif operator== 'x':
            s *= target
        elif operator== '-':
            s -= target
        elif operator== '/':
            if s<0:
                s = -(abs(s)//target)
            else:
                s//=target

    if s < mn:
        mn = s
    if s > mx:
        mx = s

print(mx)
print(mn)