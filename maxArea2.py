# 11. Container With Most Water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start = 0
        end = len(height) - 1
        while(start < end):
            maxWater = max(maxWater, min(height[start], height[end]) * (end - start))
            if height[start] > height[end]:
                end-=1
            else:
                start+=1
        return maxWater
if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print("maxArea is:", sol.maxArea(height))
