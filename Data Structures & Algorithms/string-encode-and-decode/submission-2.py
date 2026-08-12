class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = len(s)
            res += (str(count) + "#")
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        length = ""
        while i < len(s):
            if s[i] == "#":
                count = int(length)
                length = ""
                res.append(s[i+1: i+count+1 ])
                i += count + 1
            else:     
                length += s[i]
                i += 1
        return res