class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1,dp[i])
        return max(dp)

s = Solution()
test = [([0,1,0,3,2,3],4),([10,9,2,5,3,7,101,18],4),([[7,7,7,7,7,7,7],1]),([1,3,6,7,9,4,10,5,6],6)]

res = s.lengthOfLIS(test[-1][0])
print(res)
#for i in range(len(test)):
#    if not (s.lengthOfLIS(test[i][0])==test[i][1]):
#        print(test[i][0], test[i][1])

