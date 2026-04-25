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
            else:
                maxWater = max(maxWater,height[r] * (r - l))
                r -= 1
        return maxWater

if __name__ == "__main__":
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    print("maxArea is:", sol.maxArea(height))

 
    height2 = [1,1]
    print("maxArea is:", sol.maxArea(height2))
