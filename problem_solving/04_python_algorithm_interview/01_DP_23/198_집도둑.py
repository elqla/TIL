from collections import collections

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         def _rob(i:int)->int:
#             if i <0:
#                 return 0
#             return max(_rob(i-1), _rob(i-2)+ nums[i])
#         return _rob(len(nums)-1)
#

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <=2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], (nums[i]+dp[i-2]))
            #   3, 2, 5, 4, 6, 3, 5, 3, 2, 5
            #   3, 3, 8, 8, 14,14,19,19,21,24
        return dp.popitem()[1] # 딕셔너리라서, 벨류값 갖기 위함
