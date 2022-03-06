#메모이제이션
def maxSubArray(nums):
    sums = [nums[0]]
    for i in range(1, len(nums)):
        sums.append(nums[i] + (sums[i-1] if sums[i-1]>0 else 0))
    return max(sums)

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = maxSubArray(nums)
print(a)


#카데인알고리즘
import sys
def maxSubArray(nums):
    best_sum = -sys.maxsize
    current_sum = 0
    for num in nums:
        current_sum = max(num, num+current_sum)
        best_sum = max(current_sum, best_sum)
    return best_sum



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = maxSubArray(nums)
print(a)
