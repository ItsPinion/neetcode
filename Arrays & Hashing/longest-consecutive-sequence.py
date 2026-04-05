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


nums = [2, 20, 4, 10, 3, 4, 5]
solution = Solution()

print(solution.longestConsecutive(nums))
