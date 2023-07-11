class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVolume= 0
        left = 0
        right = len(height) - 1
        
        while (left < right):
            base = right - left
            tall = min(height[left], height[right])
            currVolume = tall * base

            maxVolume = max(maxVolume, currVolume)

            if height[left] == tall:
                left += 1
            else:
                right -= 1
        
        return maxVolume