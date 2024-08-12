def shell_sort1(nums: list[int]):
	# step_size = len(nums)//2
	# for gap in range(len(nums)//2, 0, step_size):
	# 	step_size /= 2
	# 	print(gap)
	gap = len(nums)//2
	while gap > 0:
		for i in range(gap, len(nums), 1):
			temp = nums[i]
			j = i
			while j >= gap and nums[j - gap] > temp:
				nums[j] = nums[j - gap]
				j -= gap
			nums[j] = temp
		gap //= 2


# nums = [9,8,7,6,6,5,4,3,2,1]
# shell_sort1(nums)
# print(nums)