class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        front = 0
        back = len(numbers) - 1

        while front < back:
            total = numbers[front] + numbers[back]

            if total == target:
                return [front+1, back+1]
            elif total < target:
                front += 1
            else:
                back -= 1

        return [0, 0]
