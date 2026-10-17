class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # dict of counters
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1

        # creating an array of counts, max size is the size of nums if every number was the same
        # if two numbers have the same count then put them in a list in this spesfic index of count
        array = [[] for _ in range(len(nums) + 1)]
        for key,value in map.items():
            array[value].append(key)
        
        res = []

        # go over the numbers from most common to least common
        for i in range(len(array)-1,-1,-1):
            if k<=0:
                return res
            # get all the nums which have the same count
            for n in array[i]:
                res.append(n)
                k-=1
        
        return res
        