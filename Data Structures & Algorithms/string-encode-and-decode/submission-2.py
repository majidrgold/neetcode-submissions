class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        str_encoded = ''.join([ f"{str(len(s))}#{s}" for s in strs])

        return str_encoded

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            sz = int(s[i:j])
            i = j + 1
            j = i + sz
            res.append(s[i:j])
            i = j

        return res

