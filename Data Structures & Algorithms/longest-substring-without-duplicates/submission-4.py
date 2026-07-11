class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {} # (character)
        l = 0
        r = 0
        max_length = 0

        while r < len(s):

            if s[r] not in hashmap:
                hashmap[s[r]] = r

            else:
                max_length = max(max_length, r - l)

                # remove the character from hashmap
                temp = hashmap.pop(s[r])

                # remove all the character before it
                for i in range(l, temp):    
                    hashmap.pop(s[i])

                # update the l pointer
                l = temp + 1

                # store the new location of character.
                hashmap[s[r]] = r

            r += 1
        
        return max(max_length, r-l)