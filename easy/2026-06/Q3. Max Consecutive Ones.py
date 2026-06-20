class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_max = 0
        lat_res = 0
        for n in nums:
            if n == 0:
                if lat_res > cur_max:
                    cur_max = lat_res
                    lat_res = 0
            else:
                lat_res += 1
        return max(lat_res, cur_max) 