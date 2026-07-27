class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a map
        prevMap = {}

        # Enumerate nums
        for index, value in enumerate(nums):
            diff = target - value

            # if diff is in map,
            if diff in prevMap:
                return [prevMap[diff], index]

            # add num and index into the map
            prevMap[value] = index