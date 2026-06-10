class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        s0 = cost[0]
        s1 = cost[1]

        for i in range(2, len(cost)):
            s0, s1 = s1, cost[i] + min(s0, s1)

        return min(s0, s1)

s = Solution()
print(s.minCostClimbingStairs([10,15,20]))