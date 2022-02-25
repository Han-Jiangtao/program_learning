class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num_1 = num1[:-1].split("+")
        num_2 = num2[:-1].split("+")
        real = int(num_1[0]) * int(num_2[0]) + int(num_1[1]) * int(num_2[1]) * -1
        vir = int(num_1[0]) * int(num_2[1]) + int(num_1[1]) * int(num_2[0])
        return str(real) + "+" + str(vir) + "i"
