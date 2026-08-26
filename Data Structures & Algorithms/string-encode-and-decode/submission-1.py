class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        sizes_part = ','.join([str(len(s)) for s in strs])
        strs_part = ''.join([s for s in strs])

        return f"{sizes_part},#{strs_part}"

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i: i + sz])
            i += sz
        
        return res

