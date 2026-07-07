class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: 
            return False
        if len(s) == 0:
            return True
        
        tempS = s.lower()
        
        startP = 0
        endP = len(tempS) - 1

        while(startP <= endP):
            char = tempS[startP]
            num = ord(char)
            if (num >= 65 and num <= 90 ) or (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                while endP >= startP:
                    num = ord(tempS[endP])
                    if (num >= 65 and num <= 90 ) or (num >= 97 and num <= 122) or (num >= 48 and num <= 57):
                        if tempS[endP] == char:
                            startP += 1
                            endP -= 1
                            break
                        else:
                            return False
                    else:
                        endP -= 1
                        continue
            else:
                startP += 1
            
        return True