class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            counter = 0
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
            if counter > 0:
                return True
        return False
            
                