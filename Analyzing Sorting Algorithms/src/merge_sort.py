def merge_sort(nums: list[int]):
    if len(nums) <= 1:
        return

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, nums)


def merge(left: list[int], right: list[int], nums: list[int]):
    left_end = len(left) - 1
    right_end = len(right) - 1

    left_index, right_index, index = 0, 0, 0
    while left_index <= left_end and right_index <= right_end:
        if left[left_index] <= right[right_index]:
            nums[index] = left[left_index]
            left_index += 1
        else:
            nums[index] = right[right_index]
            right_index += 1
        index += 1

    while left_index <= left_end:
        nums[index] = left[left_index]
        left_index += 1
        index += 1

    while right_index <= right_end:
        nums[index] = right[right_index]
        right_index += 1
        index += 1


# nums = [5, 4, 3, 2, 1]
# merge_sort(nums)
# print(nums)
