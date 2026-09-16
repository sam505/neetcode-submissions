class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            string_sort = "".join(sorted(string))
            if string_sort in anagrams:
                anagrams[string_sort].append(string)
            else:
                anagrams[string_sort] = [string]

        return list(anagrams.values())