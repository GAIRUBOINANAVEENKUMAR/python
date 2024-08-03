nums = list(map(int, input().strip().split()))
val = int(input())
new_nums = [num for num in nums if num != val]
num_removed = len(nums) - len(new_nums)
new_nums.extend(['_'] * num_removed)
print(len(new_nums))
print(new_nums)
