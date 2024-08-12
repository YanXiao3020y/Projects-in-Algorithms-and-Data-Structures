from insertion_sort import insertion_sort
from merge_sort import merge


def hybrid_sort1(nums: list[int]):
    h = int(len(nums) ** (1 / 2))
    hybrid_merge_sort(nums, h)


def hybrid_merge_sort(nums: list[int], h):
    if len(nums) > h:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        hybrid_merge_sort(left, h)
        hybrid_merge_sort(right, h)
        merge(left, right, nums)
    else:
        insertion_sort(nums)


# nums = [6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1]
# hybrid_sort1(nums)
# print(nums)
