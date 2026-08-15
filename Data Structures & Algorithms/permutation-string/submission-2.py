class Solution:
    
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        # Create hashmap of s1
        map_s1 = {}
        for c in s1:
            map_s1[c] = 1 + map_s1.get(c, 0)

        n = len(s1)

        # print(map_s1)

        # Trivial case
        if len(s1) > len(s2):
            return False

        # Pointer left and right
        l = 0
        r = n - 1

        # print(l ,r )
        # while r is still < len(s2)
        while r < len(s2):

            # hashmap of s2
            map_s2 = {}
            for c in s2[l : r+1]:
                map_s2[c] = 1 + map_s2.get(c, 0)

            print(map_s2)
            
            # compare two map
            if map_s1 == map_s2:
                return True
            
            # Increase by one both pointer
            l += 1
            r += 1

        return False
    
    def checkInclusion(self, s1:str, s2:str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ar_s1 = [0] * 26
        ar_s2 = [0] * 26

        for i in range(len(s1)):
            ar_s1[ord(s1[i]) - ord("a")] += 1
            ar_s2 [ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if ar_s1[i] == ar_s2[i] else 0

        l = 0
        for r in range(len(s1), len(s2), 1):
            if matches == 26:
                return True
            
            # check the right
            index_char_at_r = ord(s2[r]) - ord("a")
            ar_s2[index_char_at_r] += 1
            if ar_s2[index_char_at_r] == ar_s1[index_char_at_r]:
                matches += 1
            elif ar_s2[index_char_at_r] == ar_s1[index_char_at_r] + 1: # they were equal before
                matches -= 1
            
            # check the left: 
            index_char_at_l = ord(s2[l]) - ord("a")
            ar_s2[index_char_at_l] -= 1
            if ar_s1[index_char_at_l] == ar_s2[index_char_at_l]:
                matches += 1
            elif ar_s1[index_char_at_l] - 1 == ar_s2[index_char_at_l]: # they were equal before the decrement
                matches -= 1
            
            l+= 1
        return matches == 26