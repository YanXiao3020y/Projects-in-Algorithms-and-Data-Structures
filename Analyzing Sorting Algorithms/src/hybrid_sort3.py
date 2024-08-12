from hybrid_sort1 import hybrid_merge_sort


def hybrid_sort3(nums: list[int]):
    h = int(len(nums) ** (1 / 6))
    hybrid_merge_sort(nums, h)


# nums = [6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1, 6, 7, 8, 9, 5, 4, 3, 2, 1]
# hybrid_sort3(nums)
# print(nums)
