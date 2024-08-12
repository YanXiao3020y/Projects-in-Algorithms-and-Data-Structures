from hybrid_sort1 import hybrid_merge_sort


def hybrid_sort2(nums: list[int]):
    h = int(len(nums) ** (1 / 4))
    hybrid_merge_sort(nums, h)


# nums = [6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1]
# hybrid_sort2(nums)
# print(nums)
