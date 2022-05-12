#n/2 이상인 수 = 2번째
#arraylist

# while num2 == num/2>0:
#     num3 = num - num2
#     num4 = num2 - num3



# 100 입력
a = int(input())
while a//2 < a:  ####
    max_arr = [1]
    arr = []
    for b in range(a//2):  #어차피 a의 반보다 큰 수로만 돌거니까
        arr.append(a)
        arr.append(b+a//2)
        for i in range(b):
            arr[i+2] = arr[i] - arr[i+1]
            if arr[i+2] > 0 and arr[i+2] not in arr:
                arr.append(arr[i+2])
        else:
            break
    if len(arr) > len(max_arr):
        max_arr = arr
    print(len(max_arr), max_arr)


