class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num1_binary = self.convert_to_binary(num1)
        num2_binary = self.convert_to_binary(num2)

        set_bits = 0
        for digit in num2_binary:
            set_bits += int(digit)
        ans = ""

        # Taking care of most valuable 1's
        for digit in num1_binary:
            if digit == "1" and set_bits > 0:
                ans += "1"
                set_bits -= 1
            else:
                ans += "0"
        # Taking care of least valuable zero's
        for i in range(len(num1_binary) - 1, 0, -1):
            if ans[i] == "0" and set_bits > 0:
                print("Yes", len(num1_binary) - 1 - i)
                ans = ans[:i] + "1" + ans[i + 1:]
                set_bits -= 1
        # Adding the remaining ones to the end
        ans += "1" * set_bits
        return self.convert_from_binary(ans)
    
    def convert_from_binary(self, num):
        ans = 0
        for i in range(len(num)):
            ans += int(num[i]) * 2 ** (len(num) - i - 1)
        return ans

    def convert_to_binary(self, num):
        ans = ""
        while(num > 0):
            ans += str(num % 2)
            num = num // 2
        return ans[::-1]
