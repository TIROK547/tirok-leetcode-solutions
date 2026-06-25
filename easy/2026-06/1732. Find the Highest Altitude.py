class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur, cur_max = 0, 0
        for a in gain:
            cur += a
            if cur > cur_max:
                cur_max = cur
        return cur_max

