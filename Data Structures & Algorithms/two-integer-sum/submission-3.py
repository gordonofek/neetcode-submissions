class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while(i<len(nums)):
            first = nums[i]
            j=i+1
            while(j<len(nums)):
                if(first + nums[j] == target):
                    return [i,j]
                j+=1
            i+=1
        