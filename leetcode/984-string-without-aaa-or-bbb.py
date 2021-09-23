# https://leetcode.com/problems/string-without-aaa-or-bbb/


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a > 0 or b > 0:
            add_a = False
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                # Must write a different char from the prev
                add_a = True if ans[-1] == "b" else False
            else:
                add_a = True if a > b else False

            if add_a:
                ans.append("a")
                a -= 1
            else:
                ans.append("b")
                b -= 1
        return "".join(ans)
