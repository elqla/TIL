import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
vlst = [list(map(int, input().split())) for _ in range(n)]
print(vlst)
