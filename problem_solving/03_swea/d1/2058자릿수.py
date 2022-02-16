arr = list(map(int, input()))

cnt = 0
for a in arr:
    cnt += int(a)
print(cnt)


#다른방법
def sum_of_digit(num):
    total = 0
    while num>0:
        total += num%10
        num = num//10
    return total
num = int(input())
print(sum_of_digit(num))
