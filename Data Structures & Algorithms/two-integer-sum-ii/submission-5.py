class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2. Binary Search
        n = len(numbers)
        for i in range(n):
            compl = target - numbers[i]
            l, r = i + 1, n - 1
            while l <= r:
                mid = (l + r) // 2
                if compl > numbers[mid]:
                    l = mid + 1
                elif compl < numbers[mid]:
                    r = mid - 1
                else:
                    return [i + 1, mid + 1]
            
        return []

        # ---
        # # * 4. Two Pointer:Majid
        # l, r = 0, len(numbers) - 1

        # while l < r:
        #     cur_sum = numbers[l] + numbers[r] 
        #     if cur_sum < target:
        #         l += 1
        #     elif cur_sum > target:
        #         r -= 1
        #     else:
        #         return [l + 1, r + 1]
            
        # return []
        # # t: O(n), s:O(1)
        # ---


        