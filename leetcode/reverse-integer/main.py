class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1
        rev = 0
        while x != 0:
            if rev * 10 < INT_MIN + 1 or rev * 10 > INT_MAX:
                return 0
            digit = x % 10 if x > 0 else -(-x % 10)
            x = x // 10 if x > 0 else -(-x // 10)
            rev = rev * 10 + digit
        return rev
