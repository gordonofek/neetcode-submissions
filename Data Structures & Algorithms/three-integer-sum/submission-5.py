class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        map = {}
        res = []
        nums.sort()
        for i in range(len(nums)):
            map[nums[i]] = i

        for i in range(len(nums)):
            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                # Skip duplicate values for the second number
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                delta = 0 - (nums[i]+nums[j])
                if delta in map and nums[j] <= delta and map[delta] > j:
                    triplet = [nums[i],nums[j],delta]
                    res.append(triplet)
                        
        return res
