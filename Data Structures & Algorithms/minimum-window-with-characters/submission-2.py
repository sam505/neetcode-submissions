class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
         if T > S return ''
         use hash map for s with the count of each letter
         loop through the letter in t checking if any is in t hash, 
         find one and that's the start, loop keep adding letters to a 
         window_hash making sure the count does not get bigger than what 
         we have in t_hash until we find the same hash as T, update the 
         length of the window and also update the window chars.

         Move on to the next letter in the window that exists in t_hash and 
         mark it as the start and repeat the process above until we reach the 
         end of the string.

         Keep checking if the hash matches, if they do then check if the window 
         length is smaller and then update the window chars

         return the window chars
        """

        need = Counter(t)
        missing = len(t)
        left = 0
        best_start, best_len = 0, float("inf")

        for right, char in enumerate(s):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1

            while missing == 0:
                if right - left + 1 < best_len:
                    best_start, best_len = left, right - left + 1
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float("inf") else s[best_start:best_start + best_len]


        