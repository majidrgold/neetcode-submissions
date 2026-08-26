class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        sizes_part = ','.join([str(len(s)) for s in strs])
        strs_part = ''.join([s for s in strs])

        return f"{sizes_part}#{strs_part}"

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        hash_ind = s.find("#")
        sizes = [int(st) for st in s[:hash_ind].split(",")]

        strs = s[hash_ind+1:]

        index = 0
        for sz in sizes:
            res.append(strs[index : index + sz])
            index += sz
        
        return res

