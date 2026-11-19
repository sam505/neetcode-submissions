from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        candidates = deque()
        result = []

        for i, num in enumerate(nums):
            while candidates and nums[candidates[-1]] <= num:
                candidates.pop()
            candidates.append(i)

            if candidates[0] <= i - k:
                candidates.popleft()
            if i >= k - 1:
                result.append(nums[candidates[0]])
        return result