def threeSum(nums):
    nums.sort()  # Step 1: Sort the array
    result = []
    
    for i in range(len(nums) - 2):  # Step 2: Fix one element
        if i > 0 and nums[i] == nums[i - 1]:  # Step 3: Skip duplicates
            continue
        
        left, right = i + 1, len(nums) - 1  # Step 4: Two-pointer approach
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicates
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result
