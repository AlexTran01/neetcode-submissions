class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # (character)
        l = 0
        r = 0
        max_length = 0

        if(len(s) <= 1):
            return len(s)
        while r < len(s):
            if s[r] not in hashmap:
                hashmap[s[r]] = r
            else:
                max_length = max(max_length, r - l)
                temp = hashmap.pop(s[r])

                for i in range(l, temp):    
                    hashmap.pop(s[i])
                l = temp + 1

                hashmap[s[r]] = r

            r += 1
        
        return max(max_length, r-l)