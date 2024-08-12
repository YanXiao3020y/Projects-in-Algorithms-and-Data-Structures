import math
def compute_sequence_a033622(size: int):
    gap = list()
    for i in range(size):
        if i % 2 == 0: # even case
            value = 9 * 2 ** i - 9 * 2 ** (i//2) + 1
        else: # odd case
            value = 8 * 2 ** i - 6 * 2 ** ((i+1)//2) + 1
        if value < size:
            gap.append(value)

    gap.sort(reverse=True)  # sort decreasingly
    return gap


def shell_sort4(nums: list[int]):
    gap = compute_sequence_a033622(len(nums))
    for g in gap:
        for i in range(g, len(nums), 1):
            temp = nums[i]
            j = i
            while j >= g and nums[j - g] > temp:
                nums[j] = nums[j - g]
                j -= g
            nums[j] = temp


# nums = [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]
# shell_sort4(nums)
# print(nums)

