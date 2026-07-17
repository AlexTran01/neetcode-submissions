class Solution:
    def minWindow(self, s:str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        
        count_t, count_wind = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        l = 0
        have, need = 0, len(count_t)

        res, res_len = [-1, -1], float("infinity")

        for r in range(len(s)):

            c = s[r]
            count_wind[c] = 1 + count_wind.get(c, 0)

            if c in count_t and count_wind[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r] 
                    res_len = r - l + 1

                c = s[l]
                count_wind[c] -= 1
                if c in count_t and count_wind[c] < count_t[c]:
                    have -= 1
                l += 1
        
        l, r = res

        return s[l : r+1] if res_len != float("infinity") else  ""