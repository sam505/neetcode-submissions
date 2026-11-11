class Solution:
    def trap(self, height: List[int]) -> int:
        trap_water = 0
        start = 0
        end = len(height) - 1
        height_l = height_r = 0
        
        while start < end:
            if height[start] < height[end]: 
                height_l = max(height_l, height[start])
                trap_water += height_l - height[start]
                start += 1
            else:
                height_r = max(height_r, height[end])
                trap_water += height_r - height[end]
                end -= 1
                    
        return trap_water
        