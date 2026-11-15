class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        i = 0
        length = 0
        for j, char in enumerate(s):
            while char in unique:
                unique.remove(s[i])
                i += 1
            unique.add(char)
            length = max(length, j - i + 1)
        return length
