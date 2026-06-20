class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(len(nums)-n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
            
s = Solution()
res = s.shuffle([2,5,1,3,4,7],3)
print(res == [2,3,5,4,1,7])
print(res)