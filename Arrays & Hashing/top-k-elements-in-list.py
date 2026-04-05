class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency: dict[int, int] = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        print(frequency)

        return [
            num
            for num, _ in sorted(
                frequency.items(), key=lambda item: item[1], reverse=True
            )[:k]
        ]


nums = [1, 2, 2, 3, 3, 3]
k = 2

solution = Solution()
print(solution.topKFrequent(nums, k))
