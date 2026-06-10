class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = []
        for i in range(0, amount+1):
            for coin in coins:
                sp = amount - coin
                memo[sp] = memo.get(sp) + 1 if memo.get(sp) else 1
        return memo[amount]
s =Solution()
print(s.change(5, [1,2,5]))