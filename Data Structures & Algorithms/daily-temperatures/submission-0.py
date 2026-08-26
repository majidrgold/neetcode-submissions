class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                update_day, update_temp = stack.pop()
                res[update_day] = day - update_day
                
            stack.append((day, temp))

        return res

        