import pprint
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        prev = [0] * n
        curr = [0] * n

        for i in range(n-1, -1, -1):
            curr[i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    curr[j] = prev[j-1] + 2
                else:
                    curr[j] = max(prev[j], curr[j-1])

            prev = curr
            curr = [0] * n
            print(prev)
s = Solution()
res = s.longestPalindromeSubseq("total")


