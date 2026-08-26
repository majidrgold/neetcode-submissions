class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = {}
        for _str in strs:
            counter = [0]*26
            for char in _str:
                counter[ord(char) - ord('a')] += 1
            
            key = tuple(counter)
            if key not in counters:
                counters[key] = []
            counters[key].append(_str)
        
        return list(counters.values())

        # get counter of all
        # group counters togther:
        
        