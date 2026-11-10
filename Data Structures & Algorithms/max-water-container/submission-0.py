class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = len(heights) -1
        i = 0
        max_area = 0
        while i < l:
            max_area = max(max_area, (l - i) * min(heights[l], heights[i]))

            if heights[l] > heights[i]:
                i += 1
            else:
                l -= 1

        return max_area
