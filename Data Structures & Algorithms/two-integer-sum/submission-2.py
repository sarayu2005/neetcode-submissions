class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in hashmap:              # check hashmap not list
                return [hashmap[diff], i]    # diff's index, current index
            
            hashmap[n] = i 