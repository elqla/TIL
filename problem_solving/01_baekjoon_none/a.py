import sys
sys.stdin = open('input.txt', 'r')


for t in range(2):
    N = int(input())
    tmpLst = list(map(int, input().split()))
    a = int(input())


    mx = 0
    for tmp in tmpLst:
        if(a==tmp):
            mx = mx + 1
    #1 12
    #2 23
    print(f"#{t+1} {mx}") 
    print("#" + str(t+1)+ " " + str(mx))