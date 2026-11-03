class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s) == sorted(t)
      # t:[nlogn] s: [n]  