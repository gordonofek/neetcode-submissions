class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # creating counter dict
        map = {}
        for n in nums:
            if n not in map:
                map[n] = 1
            else:
                map[n] += 1
        
        array = [[] for _ in range(len(nums) + 1)]
        for n in map:
            array[map[n]].append(n)
        
        res = []
        for i in range(len(array) - 1, -1, -1):
            for num in array[i]:
                res.append(num)
                if len(res) == k:
                    return res