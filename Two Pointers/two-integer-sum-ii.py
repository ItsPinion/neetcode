class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        front = 0
        back = len(numbers) - 1

        while front < back:
            total = numbers[front] + numbers[back]

            if total == target:
                return [front + 1, back + 1]
            elif total < target:
                front += 1
            else:
                back -= 1

        return [0, 0]


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
print(solution.twoSum([2, 3, 4], 6))  # Output: [1, 3]
print(solution.twoSum([-1, 0], -1))  # Output: [1, 2]
