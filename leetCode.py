def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if j==i:
                    continue
                else:
                   print("===",nums[i],nums[j])
                   if(nums[i]+nums[j]==target):
                        return [i,j]
                   
print(twoSum([3,2,4],6))