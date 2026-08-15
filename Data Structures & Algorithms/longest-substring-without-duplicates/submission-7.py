class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # letter -> index
        longestLen = 0
        l = r = 0
        while r < len(s):

            if s[r] not in hashmap:
                hashmap[s[r]] = r
                longestLen = max(longestLen, r-l+1)

            else:
                for i in range(l, hashmap[s[r]], 1):
                    hashmap.pop(s[i])
                
                l = hashmap[s[r]] + 1
                hashmap[s[r]] = r

            r += 1

        return longestLen