import math
def compute_sequence_a003586(size: int):
    gap = list()
    max_p = int(math.log(size, 2))
    max_q = int(math.log(size, 3))
    gap = list()
    for p in range(max_p+1):
        for q in range(max_q+1):
            value = (2 ** p) * (3 ** q)
            if value <= size:
                gap.append(value)

    gap.sort(reverse=True) # sort decreasingly
    return gap


def shell_sort3(nums: list[int]):
    gap = compute_sequence_a003586(len(nums))
    for g in gap:
        for i in range(g, len(nums), 1):
            temp = nums[i]
            j = i
            while j >= g and nums[j - g] > temp:
                nums[j] = nums[j - g]
                j -= g
            nums[j] = temp


# print(compute_sequence_a003586(5000))
# nums = [9, 8, 7, 6, 6, 5, 4, 3, 2, 1]
# shell_sort3(nums)
# print(nums)
