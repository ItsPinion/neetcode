class Solution:
    def trap(self, height: list[int]) -> int:

        left: int = 0
        right: int = len(height) - 1
        maxL = height[left]
        maxR = height[right]
        water: int = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(height[left], maxL)
                water += maxL - height[left]

            else:
                right -= 1
                maxR = max(height[right], maxR)
                water += maxR - height[right]

        return water


solution = Solution()
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]

print(solution.trap(height))
