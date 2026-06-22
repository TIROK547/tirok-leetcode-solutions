class Solution:
    def numSquares(self, n: int) -> int:
        import math

        def is_perfect_square(n: int) -> bool:
            return math.isqrt(n) ** 2 == n

        def solve(n: int) -> int:
            for i in range(n, 0, -1):
                print(i)
        
        solve(n)

s = Solution()
s.numSquares(12)
