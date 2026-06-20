class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                if abs(i - seen[nums[i]]) <= k:
                    return True
            seen[nums[i]] = i
        return False
s = Solution()
print(s.containsNearbyDuplicate([0,1,2,3,4,0,0,7,8,9,10,11,12,0],1))