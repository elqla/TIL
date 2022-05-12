#n, k = map(int, input().split())
#n = 날짜의 수
#k = 연속된 날짜의 수 (1~n사이)

N, K = map(int, input().split())
tem_list = list(map(int, input().split()))

part_sum = sum(tem_list[:K])
result_list = [part_sum]

for i in range(0, len(tem_list)-K):
    part_sum = part_sum - tem_list[i] + tem_list[i+K]
    result_list.append(part_sum)

print(max(result_list))




# lst = list(map(int, input().split()))
# mx = 0
# for i in range(n-k+1):
#     tmp = 0
#     for j in range(k):
#         tmp += lst[i+j]
#     if tmp > mx:
#         mx = tmp
#
#
# print(mx)

# tmp = sum(lst[i:i+k])