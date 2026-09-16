class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        createMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in createMap:
                return [createMap[diff], i]
            createMap[n] = i
        