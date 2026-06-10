class Solution:
    def coinChange(self, coins, amount):
        def min_ignore_none(a, b):
            if a is None:
                return b
            if b is None:
                return a
            return min(a, b)

        memo = {}

        def minimum_coins(m):
            if m in memo:
                return memo[m]

            if m == 0:
                answer = 0
            else:
                answer = None

                for coin in coins:
                    subproblem = m - coin

                    if subproblem < 0:
                        continue

                    sub_answer = minimum_coins(subproblem)

                    if sub_answer is not None:
                        answer = min_ignore_none(
                            answer,
                            sub_answer + 1
                        )

            memo[m] = answer
            print(memo)
            return answer
        result = minimum_coins(amount)
        return -1 if result is None else result


s = Solution()
print(s.coinChange([1,3,5], 50))