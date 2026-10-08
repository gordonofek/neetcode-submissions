class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for n in nums:
            my_dict[n] = my_dict.get(n,0) + 1
        
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
        sorted_k_list = list(sorted_dict.items())[:k]

        res = []
        for i in range(0,k):
            res.append(sorted_k_list[i][0])
        
        return res 
        