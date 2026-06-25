class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        prev = [1] * (m+1)

        for i in range(1, n):
            curr = [0] * (m+1)
            pref = 0
            if i % 2 == 1:
                for j in range(1, m + 1):
                    curr[j] = pref
                    pref += prev[j]
            else:
                for j in range(m, 0, -1):
                    curr[j] = pref
                    pref += prev[j]
            print(prev ,curr, pref, i%2 ==0)
            prev = curr

        return sum(prev)*2


s = Solution()
print(s.zigZagArrays(3,4,5))
