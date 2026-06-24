class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n=len(nums)
        my_map = {}
        for  i in range(n):
           difference =target-nums[i]

           if difference  in my_map:
               return [my_map[difference],i]
           else:
              my_map[nums[i]]=i