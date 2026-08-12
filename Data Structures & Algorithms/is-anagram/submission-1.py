class Solution:
    def isAnagram(self, s:str, t:str)->nb:
        if len(s) != len(t):
            return False
        else:
            return sorted(s) == sorted(t)