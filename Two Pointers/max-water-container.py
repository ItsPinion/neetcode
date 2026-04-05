class Solution:
    def maxArea(self, heights: list[int]) -> int:
        f, b = 0, len(heights) - 1

        maximum_area: int = min(heights[f], heights[b]) * (b - f)

        while f < b:
            if heights[f] > heights[b]:
                b -= 1
            else:
                f += 1
            area = min(heights[f], heights[b]) * (b - f)
            if maximum_area < area:
                maximum_area: int = area

        return maximum_area


solution = Solution()

print(
    solution.maxArea(
        [1, 7, 1, 1, 1, 1, 2, 5, 12, 3, 500, 50, 7, 8, 4, 7, 38, 9, 10, 12, 6]
    )
)  # Output: 500 (the container formed by the lines at index 0 and index 10 has the most water, with an area of 500)
print(
    solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
)  # Output: 49 (the container formed by the lines at index 1 and index 8 has the most water, with an area of 49)
