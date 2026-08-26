class Solution:
    def trap(self, height: List[int]) -> int:
        # if not height:
        #     return 0

        # bars = len(height)
        # prefix = [0] * bars
        # suffix = [0] * bars

        # prefix[0] = height[0]
        # for i in range(1, bars):
        #     prefix[i] = max(height[i], prefix[i - 1])

        # suffix[-1] = height[-1]
        # for i in range(bars - 2, -1 , -1):
        #     suffix[i] = max(height[i], suffix[i+1])
        # trapped_water = 0
        # for i in range(bars):
        #     trapped_water += min(suffix[i], prefix[i]) - height[i]
        
        # return trapped_water

        # optimized:
        if not height:
            return 0

        bars = len(height)
        prefix = [0] * bars
        suffix = [0] * bars

        suffix[-1] = height[-1]
        for i in range(bars - 2, -1 , -1):
            suffix[i] = max(height[i], suffix[i+1])

        prefix = height[0]
        trapped_water = 0
        for i in range(1, bars):
            prefix = max(height[i], prefix)
            trapped_water += min(suffix[i], prefix) - height[i]
        
        return trapped_water