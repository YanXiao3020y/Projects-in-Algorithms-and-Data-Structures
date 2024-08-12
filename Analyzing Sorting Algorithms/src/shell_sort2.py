def compute_sequence_a083318(size: int):
    gap = list()
    gap.append(1) # default value a(0) = 1
    for k in range(1, size):
        value = 2 ** k + 1
        gap.append(value)

    gap.sort(reverse=True)  # sort decreasingly
    return gap


def shell_sort2(nums: list[int]):
    gap = compute_sequence_a083318(len(nums))
    for g in gap:
        for i in range(g, len(nums), 1):
            temp = nums[i]
            j = i
            while j >= g and nums[j - g] > temp:
                nums[j] = nums[j - g]
                j -= g
            nums[j] = temp

# print(compute_sequence_a083318(50))
# nums = [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]
# shell_sort2(nums)
# print(nums)
