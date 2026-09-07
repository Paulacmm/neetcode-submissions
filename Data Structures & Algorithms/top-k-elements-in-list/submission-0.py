class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}

        for n in nums:
            nums_map[n] = 0

        for n in nums:
            nums_map[n] += 1

        sorted_map = dict(sorted(nums_map.items(), key=lambda item: item[1], reverse = True))

       
        result  = list(sorted_map.keys())[:k]

        return result