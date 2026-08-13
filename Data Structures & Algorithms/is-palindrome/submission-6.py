class Solution:

    def isNonAlphanumeric(self,num: int) -> bool:
        return (num >= 65 and num <= 90 ) or (num >= 97 and num <= 122) or (num >= 48 and num <= 57)

    def isPalindrome(self, s: str) -> bool:
        if not s: 
            return False
        if len(s) == 0:
            return True
        
        tempS = s.lower()
        
        startP = 0
        endP = len(tempS) - 1

        while startP < endP:
            while startP < endP and not self.isNonAlphanumeric(ord(tempS[startP])) :
                startP += 1
            while endP > startP and not self.isNonAlphanumeric(ord(tempS[endP])):
                endP -= 1
            if tempS[endP] != tempS[startP]:
                return False
            else:
                startP += 1
                endP -= 1
        
    
        return True