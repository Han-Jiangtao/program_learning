class Solution:
    def addDigits(self, num: int) -> int:
        num_str = str(num)
        while len(num_str) > 1:
            sum_num = 0
            for item in num_str:
                sum_num += int(item)
            num_str = str(sum_num)
        return int(num_str)
