import sys


def extrapolate(nums):
    if nums:
        yield nums[-1]
        yield from extrapolate(
            [num2 - num1 for num1, num2 in zip(nums, nums[1:])]
        )


histories = [[int(num) for num in line.split()] for line in sys.stdin]

print("Part 1:", sum(sum(extrapolate(nums)) for nums in histories))
print("Part 2:", sum(sum(extrapolate(nums[::-1])) for nums in histories))
