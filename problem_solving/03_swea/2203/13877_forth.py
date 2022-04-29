

t= int(input())
for tc in range(1, t+1):
    lst = input().split()

    no_number = ['/','*','+','-','.']
    stack = []
    res = 0
    for l in lst:
        if l not in no_number:
            stack.append(int(l))
        else:
            try:
                if l != '.':
                    b = stack.pop() # 먼저 뽑지만, 우측에 위치
                    a = stack.pop()
                    if l=='+':
                        c = a+b
                        stack.append(c)
                    elif l=='*':
                        c = a*b
                        stack.append(c)
                    elif l=='/':
                        c = a//b
                        stack.append(c)
                    elif l=='-':
                        c = a-b
                        stack.append(c)
                else:
                    if len(stack)!=1: # stack에 값이 2개 이상남아있어, 연산이 완료되지 않았을때
                        res = 'error'
                    else:
                        res = stack.pop()
                        break
            except:  # pop error
                res = 'error'


    print(f'#{tc} {res}')





'''
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
 


'''

















