def twoSum(self, nums, target):
      newSet = {}
      for i in range(len(nums)):
         if target - nums[i] in newSet:
            return [newSet[target - nums[i]],i]
         else:
            newSet[nums[i]]=i