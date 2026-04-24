#11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxWater = 0
        while l < r:
            if(height[l] < height[r]):
                maxWater = max(maxWater,height[l] * (r - l))
                l += 1
