class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for i in range(num1, num2 + 1):
            str_num = str(i)
            for j in range(1, len(str_num)-1):
                cur_n = int(str_num[j])
                pre_n = int(str_num[j-1])
                nex_n = int(str_num[j+1])
                #check for peak
                if pre_n < cur_n and nex_n < cur_n:
                    waviness += 1
                #check fot valley
                elif pre_n > cur_n and nex_n > cur_n:
                    waviness += 1
        print(waviness)

c = Solution()
c.totalWaviness(6047883,6535108)
