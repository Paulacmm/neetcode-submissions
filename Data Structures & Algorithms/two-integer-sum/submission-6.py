class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = {}

        for i, num in enumerate(nums):
            map_nums[num] = i

        for i, num in enumerate(nums):
            sub = target - num
            if sub in map_nums and map_nums[sub] != i:
                return [i, map_nums[sub]]