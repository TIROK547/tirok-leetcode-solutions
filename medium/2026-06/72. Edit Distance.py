class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        prev = []
        curr = [0] * (n+1)
        curr[0] = 1

        for i in range(n+1):
            prev.append(i)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = min(prev[j], prev[j-1], curr[j-1])+1
            prev = curr
            curr = [0] * (n+1)
            curr[0] = prev[0]+1
        return prev[n]


s = Solution()
res = s.minDistance("horse", "ros")
print(res)
