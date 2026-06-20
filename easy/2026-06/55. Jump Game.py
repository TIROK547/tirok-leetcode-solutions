class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        for i in range(n):
            for j in range(i+1, min(nums[i]+i,n)):
                dp[j] = True
                print(i, j)
        return dp[n-1]

s = Solution()
res = s.canJump([3,2,1,0,4])
print(res)
