class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(key=lambda p: p[0], reverse=True)
        count = 0
        curr_time= 0

        for i,(pos,spe) in enumerate(pairs):
            time = (target-pos) / spe
            if i == 0:
                curr_time = time
                count += 1

            if time > curr_time:
                count += 1
                curr_time = time
                

        return count
