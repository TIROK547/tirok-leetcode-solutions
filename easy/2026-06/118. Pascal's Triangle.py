class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(1, numRows):
            cur_row = [0] * i
            cur_row[-1], cur_row[0] = 1, 1

            dp.append(cur_row)
        
        for i in range(1, numRows):
            for j in range(1, i):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        print(dp)

