class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        length = 0
        chars = {}
        for j, char in enumerate(s):
            chars[char] = chars.get(char, 0) + 1
            if (j - i + 1) - max(chars.values()) <= k:
                length = max(length, j - i + 1)
            else:
                chars[s[i]] = chars.get(s[i]) - 1
                i += 1

        return length
