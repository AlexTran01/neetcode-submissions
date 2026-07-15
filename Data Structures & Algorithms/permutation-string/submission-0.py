class Solution:
    
  def checkInclusion(self, s1: str, s2: str) -> bool:
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
        # Create hashmap of s1
        map_s1 = {}
        for c in s1:
            map_s1[c] = 1 + map_s1.get(c, 0)

        n = len(s1)

        # Trivial case
        if len(s1) > len(s2):
            return False

        # Pointer left and right
        l = 0
        r = 0
        # increase r to n character
        for i in range(n):
            r += 1

        # while r is still < len(s2)
        while r:

            # hashmap of s2
            map_s2 = {}
            for c in s2[l : r+1]:
                map_s2[c] = 1 + map_s2.get(c, 0)
            
            # compare two map
            if map_s1 == map_s2:
                return True
            
            # Increase by one both pointer
            l += 1
            r += 1

        return False