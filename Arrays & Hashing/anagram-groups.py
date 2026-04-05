class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:

        anagrams: list[list[str]] = []

        while len(strs) > 0:
            anagram = [strs[0]]

            for word in strs[1:]:
                if self.isAnagram(anagram[0], word):
                    anagram.append(word)

            for word in anagram:
                strs.remove(word)

            anagrams.append(anagram)

        return anagrams


strs = ["act", "pots", "tops", "cat", "stop", "hat"]

solution = Solution()
print(solution.groupAnagrams(strs))
