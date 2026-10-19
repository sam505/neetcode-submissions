class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        k = number of unique most frequent elements
        """
        count = {}

        elements = [[] for n in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            elements[c].append(n)

        res= []
        for i in range(len(elements), 0, -1):
            res.extend(elements[i - 1])
            if len(res) == k:
                return res

        

        