class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for i in nums:
            if i not in hashset:
                hashset.add(i)
        if len(nums)==len(hashset):
            return False
        else:
            return True
        