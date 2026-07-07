class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = len(s)
            res = res + f"{count}#{s}" 
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        placeholder = ""
        i = 0
        while(i < len(s)): # in range loop does not allow for dynamically indices skip. so we have to use while loop
            if s[i] != "#":
                # getting the count 
                placeholder += s[i]
                i += 1
            else: 
                # meet the dilimeter 
                print(placeholder)
                count = int(placeholder)
                res.append(s[i+1 : i+count+1])
                #reset
                i = i + count + 1  # don't forget to skip ahead (count+1) position to get to the next start number.
                placeholder = "" # reset the place holder.
        return res