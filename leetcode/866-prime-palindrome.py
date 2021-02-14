import math


class Solution:
    def is_prime(self, N: int) -> bool:
        if N == 1:
            return False
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False
        return True

    def primePalindrome(self, N: int) -> int:
        for digits in range(1, 6):
            # Check for odd-length paliindromes
            for s in range(10 ** (digits - 1), 10 ** digits):
                s = str(s)
                x = int(s + s[-2::-1])  # eg. s = '123' -> x = int('123' + '21')
                if x >= N and self.is_prime(x):
                    return x
            # Check for even-length palindromes
            for s in range(10 ** (digits - 1), 10 ** digits):
                s = str(s)
                x = int(s + s[-1::-1])  # eg. s = '123' -> x = int('123' + '321')
                if x >= N and self.is_prime(x):
                    return x
        return ans


if __name__ == "__main__":
    print(Solution().primePalindrome(9989900))
