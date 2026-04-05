class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


solution = Solution()
print(solution.isAnagram("listen", "silent"))  # Output: True
print(solution.isAnagram("hello", "world"))  # Output: False
