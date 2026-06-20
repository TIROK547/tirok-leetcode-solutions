class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            cur_row = [0] * i
            cur_row[-1], cur_row[0] = 1, 1

            dp.append(cur_row)
        print(dp)

