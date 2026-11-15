class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        s1_hash = {}
        for char in s1:
            s1_hash[char] = s1_hash.get(char, 0) + 1
        i = 0
        j = i + len(s1)
        while j <= len(s2):
            perm_hash = {}
            for char in s2[i: j]:
                perm_hash[char] = perm_hash.get(char, 0) + 1
            if perm_hash == s1_hash:
                return True
            i += 1
            j += 1
        return False
