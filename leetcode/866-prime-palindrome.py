import math


class Solution:
    def isPrime(self, N: int) -> bool:
        if N == 1:
            return False
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                return False
        return True

    def isPalindrome(self, N: int) -> bool:
        N = str(N)
        if len(N) == 1:
            return True
        for i in range(0, len(N)):
            if i != math.ceil(len(N) / 2) and N[i] != N[-(i + 1)]:
                return False
        return True

    def primePalindrome(self, N: int) -> int:
        for ans in range(N, 10 ** 8 * 2):
            # print(ans)
            if self.isPalindrome(ans) and self.isPrime(ans):
                break
        return ans


if __name__ == "__main__":
    print(Solution().primePalindrome(13))
