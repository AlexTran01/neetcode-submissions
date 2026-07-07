class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = [] # list of list 

        for s in strs:
            groupExist = False

            for list in result:
                # there is the anagram already that this str belong to.
                if sorted(list[0]) == sorted(s):
                    list.append(s)
                    groupExist = True
                    break
                else:
                    continue
            
        
            if not groupExist:
                result.append([s])
                
        return result