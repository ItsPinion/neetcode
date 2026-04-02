class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output: list[int] = []

        product = 1

        for num in nums:
            product *= num

        for num in nums:
            output.append(product // num)

        return output
