class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        track = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while track and h < track[-1][1]:
                idx, height = track.pop()
                area = (i - idx) * height
                max_area = max(area, max_area)
                start = idx
                
            track.append((start, h))
        
        for i, h in track:
            max_area = max((len(heights) - i) * h, max_area)


        return max_area

