class TimeMap:

    def __init__(self):
       self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        valueList = self.timeMap[key]
        l, r = 0, len(valueList)
        res = ""
        while l < r:
            mid = l + (r-l) // 2

            if valueList[mid][0] == timestamp:
                return valueList[mid][1]
            elif timestamp <= valueList[mid][0]:
                r = mid
            else: 
                res = valueList[mid][1]
                l = mid + 1

        return res