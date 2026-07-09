class Solution:
    def trap(self, heights: List[int]) -> int:
        if len(heights) < 3: return 0
        limit = 0
        l, r = 0, len(heights) - 1
        trapRainWater = min(heights[l], heights[r]) * (l - r - 1)

        while (l < r):
            addArea = 0
            takeAway = 0
            if heights[l] > limit or heights[r] > limit:
                addArea = min(heights[l]-limit, heights[r]-limit) * (r-l-1)
                if addArea >= 0: 
                    takeAway += limit
                else:
                    takeAway = 0
                    addArea = 0
            if heights[l] < limit:
                takeAway += heights[l]
            if heights[r] < limit:
                takeAway += heights[r]
            trapRainWater = trapRainWater + addArea - takeAway
            print(f"addArea: {addArea}")
            print(f"takeAway: {takeAway}")
            limit = max(min(heights[l], heights[r]), limit)
            print(f"limit: {limit}")
            print(f"trapRain: {trapRainWater}")
            print(f"l: {l}")
            print(f"r: {r}")
            print("\n")

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return trapRainWater