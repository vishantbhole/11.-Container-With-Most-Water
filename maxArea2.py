# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        while(start < end):
            maxWater = max(maxWater, min(height[start], height[end]) * (end - start))
            if height[start] > height[end]:
                end-=1
