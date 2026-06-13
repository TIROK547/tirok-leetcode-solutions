class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        r1, r2 = nums[0], max(nums[0], nums[1])
        for i in range(2,len(nums)):
            cur = nums[i] + r1
            if cur < r2:
                cur = r2
            r1 = r2
            r2 = cur
        return max(r1, r2)
