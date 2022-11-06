class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prevDays = []
        ans = [0 for i in range(len(temperatures))]
        for i, t in enumerate(temperatures):
            while len(prevDays) > 0 and prevDays[-1][1] < t:  # warmer
                prev_i, _ = prevDays.pop()
                ans[prev_i] = i - prev_i
            prevDays.append((i, t))
        return ans
