class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0 :
            return False
        target = s//2
        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for s in range(target - num, -1, -1):
                print(s, num)
                if dp[s]:
                    dp[s+num] = True
        print(dp)
        return dp[target]

s = Solution()
r= s.canPartition([1,5,11,5])
print(r)
