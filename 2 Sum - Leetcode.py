def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if num in lookup:
            return [lookup[num], i]
        lookup[target - num] = i
