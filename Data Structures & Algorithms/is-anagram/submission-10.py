class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1
        for char in t:
            if (char not in counts) or (counts[char] <= 0):
                return False
            else:
                counts[char] -= 1
        return all(item[1] == 0 for item in counts.items())

        # O(n), O(n)

sol = Solution()
print(sol.isAnagram(s = "racecar", t = "carrace"))
print(sol.isAnagram(s = "jar", t = "jam"))
print(sol.isAnagram(s = "x", t = "x"))
print(sol.isAnagram(s = "", t = "carrace"))


        


        