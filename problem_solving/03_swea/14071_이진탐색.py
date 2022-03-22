def inorder(node):
    global cnt
    if node < n+1:
        inorder(node*2)
        tree[node] = cnt
        cnt += 1
        inorder(node*2+1)


T = int(input())
for t in range(1, T+1):
    n = int(input())

    tree=[0]*(n+1)
    cnt = 1 #node인자값
    inorder(1) #node
    print(tree)
    print(f'#{t} {tree[1]} {tree[n//2]}')






'''
3
6
8
15
'''


