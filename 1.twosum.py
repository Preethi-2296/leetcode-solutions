class Solution(object):
    def twoSum(self, nums, target):
        for j in range(len(nums)):
            for k in range(j):
                if (nums[j]+nums[k]==target):
                    return [j,k]
            
        return []
        
