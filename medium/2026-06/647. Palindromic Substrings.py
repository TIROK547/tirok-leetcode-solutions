class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        memo = {}
        def is_pld(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= j:
                memo[(i, j)] = True
                return True

            if s[i] != s[j]:
                memo[(i, j)] = False
                return False

            memo[(i, j)] = is_pld(i + 1, j - 1)
            return memo[(i, j)]


        for i in range(n):
            for j in range(i, n):
                if is_pld(i, j):
                    count+=1

        return count

s = Solution()
res = s.countSubstrings("abc")
print(res)
