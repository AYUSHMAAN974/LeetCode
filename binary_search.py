class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low=0
        high=len(nums)-1
        def bs(nums, low, high):
            if low<=high:
                mid=(low+high)//2
                if nums[mid]<target:
                    low=mid+1
                    return bs(nums,low,high)
                
                elif nums[mid]>target:
                    high=mid-1
                    return bs(nums,low,high)
                elif nums[mid]==target:
                    return mid
            else:
                return -1

        val=bs(nums,low,high)
        return val
