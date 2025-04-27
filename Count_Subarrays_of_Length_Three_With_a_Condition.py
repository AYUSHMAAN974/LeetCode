class Solution(object):
    def countSubarrays(self, nums):
        count=0
        for i in range(len(nums)-2):
            check=(nums[i]+nums[i+2])*2
            if nums[i+1]==check:
                count+=1        
            
        return count
