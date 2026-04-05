class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for num in set(nums):
            complement = target - num
            if complement in set(nums):
                num_index = nums.index(num)
                if complement == num:
                    complement_index = nums.index(complement, num_index + 1)
                else:
                    complement_index = nums.index(complement)
                return sorted([num_index, complement_index])

        return []


solution = Solution()
print(solution.twoSum([-3, 4, 3, 90], 0))  # Output: [0, 2]
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))  # Output: [1, 2]
