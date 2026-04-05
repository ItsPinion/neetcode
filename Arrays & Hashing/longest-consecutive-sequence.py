class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                i = num
                count = 1
                while i in nums_set:
                    count += 1

                    i += 1

                if longest < count:
                    longest = count

        return longest


solution = Solution()
print(
    solution.longestConsecutive([2, 20, 4, 10, 3, 4, 5])
)  # Output: 4 (the longest consecutive sequence is [2, 3, 4, 5])
print(
    solution.longestConsecutive([1, 9, 3, 10, 4, 20, 2])
)  # Output: 4 (the longest consecutive sequence is [1, 2, 3, 4])
