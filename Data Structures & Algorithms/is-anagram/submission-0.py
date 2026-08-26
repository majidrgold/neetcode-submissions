class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            if char in counter:
                counter[char] -= 1
            else:
                return False
        for k in counter:
            if counter[k] != 0:
                return False

        return True
        