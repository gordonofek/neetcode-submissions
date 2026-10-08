class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {nums[i]: i for i in range(len(nums))}
        for i in range(len(nums)):
            check = target - nums[i]
            if(check in num_map and i != num_map[check]):
                return [i,num_map[check]]
        
        
        