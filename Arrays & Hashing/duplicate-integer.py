class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        return len(set(nums)) != len(nums)

solution = Solution()
print(solution.hasDuplicate([1, 2, 3, 4, 5]))  # Output: False
print(solution.hasDuplicate([1, 2, 3, 4, 5, 2]))  # Output: True