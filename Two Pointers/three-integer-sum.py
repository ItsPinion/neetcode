class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = []

        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            front, back = i + 1, len(nums) - 1

            while front < back:
                total = num + nums[front] + nums[back]

                if total > 0:
                    back -= 1
                elif total < 0:
                    front += 1
                else:
                    result.append([num, nums[front], nums[back]])

                    front += 1
                    back -= 1

                    while nums[back] == nums[back + 1] and front < back:
                        back -= 1

        return result


solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
print(solution.threeSum([]))  # Output: []
print(solution.threeSum([0]))  # Output: []
