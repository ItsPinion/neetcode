w = [3, 5, 6, 7]
k = 15


def test(current_elements: list[int], index: int):
    total = sum(current_elements)

    if total == k:
        print(current_elements)
        return

    if total > k or index >= len(w):
        return

    # INCLUDE current element
    test(current_elements + [w[index]], index + 1)

    # EXCLUDE current element
    test(current_elements, index + 1)


test([], 0)


def sum(nums: list[int]) -> int:
    if len(nums) == 0:
        return 0
    return nums[0] + sum(nums[1:])
