class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        temp = 1

        output: list[int] = []

        for num in nums:
            output.append(temp)
            temp *= num

        temp = 1

        for i, num in enumerate(nums[::-1]):
            output[len(nums) - i - 1] *= temp
            temp *= num

        return output


solution = Solution()
print(solution.productExceptSelf([-1, 0, 1, 2, 3]))  # Output: [0, 6, 0, 0, 0]
print(solution.productExceptSelf([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
