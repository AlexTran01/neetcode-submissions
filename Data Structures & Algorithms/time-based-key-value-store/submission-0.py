class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key] = self.map.get(key, {})
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key, {})
        res = ""
        print(values)
        if not values:
            print("empty")
            return ""

        timestamps = list(values.keys())
        print (timestamps)
        print(timestamp)
        l = 0 
        r = len(timestamps) - 1
        while l <= r:
            mid = l + (r-l)//2
            # print(f"mid: {mid}, l: {l}, r: {r}")

            if timestamps[mid] <= timestamp:
                res = values[timestamps[mid]]
                l = mid + 1
            else:
                r = mid - 1
        return res
    


        
