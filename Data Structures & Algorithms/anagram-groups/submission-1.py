class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = defaultdict(list) # hashmap -> list of same anagrams

        for s in strs:
            hashmap[str(sorted(s))].append(s)
        
        return list(hashmap.values())
           
