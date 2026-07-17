class Solution:
    def minWindow(self, s:str, t: str) -> str:
        if t == "" or len(s) < len(t):
            return ""
        # create hashmap that store the count of character of t and current window
        count_t, count_wind = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        res, res_len = [-1, -1], float("infinity") # store the length of infinty to find the min substring easier.
        have, need = 0, len(count_t) # have == need means the substring contains aleast all character of t

        l = 0
        for r in range(len(s)):
            c = s[r]
            count_wind[c] = 1 + count_wind.get(c, 0)

            if c in count_t and count_wind[c] == count_t[c]: # the first time count of c == with the count of c in t
                have += 1
            
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r] 
                    res_len = r - l + 1

                c = s[l]
                count_wind[c] -= 1
                if c in count_t and count_wind[c] < count_t[c]:
                    have -= 1

                l += 1  # l will end at 1 position after the needed position. It is fine as r have to meet the character at l-1 unorder to have == need again
        
        l, r = res

        return s[l : r+1] if res_len != float("infinity") else  ""