class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, c = 0, 0
        for n in nums:
            if n % 3 == 0 and n % 2 == 0:
                s += n
                c += 1
        return s // c if c > 0 else 0
