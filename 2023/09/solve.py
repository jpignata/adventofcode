import sys


def extrapolate(nums):
    tails = []

    while any(nums):
        tails.append(nums[-1])
        nums = [num2 - num1 for num1, num2 in zip(nums, nums[1:])]

    return sum(tails)


sequences = [[int(num) for num in line.split()] for line in sys.stdin]

print("Part 1:", sum(extrapolate(nums) for nums in sequences))
print("Part 2:", sum(extrapolate(nums[::-1]) for nums in sequences))
