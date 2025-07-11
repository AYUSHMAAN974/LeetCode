class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        high=len(nums)-1
        mini=float('inf')
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            elif nums[low]<=nums[mid]:
                mini=min(mini,nums[low])
                low=mid+1
        return mini  
