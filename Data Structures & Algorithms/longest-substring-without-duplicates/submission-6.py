class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # letter -> index
        longestLen = 0
        l = 0
        for i,c in enumerate(s):

            if c in hashmap:
                index = hashmap[c]
                # pop all element upuntil old "c"
                for x in s[l : index]:
                    hashmap.pop(x)

                hashmap[c] = i
                l = index + 1
            else:
                hashmap[c] = i
                longestLen = max(i - l + 1, longestLen)

        return longestLen