import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # creating Max heap using neg values of Min heap
        negList = list(map(lambda x: -x, stones))
        heapq.heapify(negList)

        while(len(negList)>1):
            x = heapq.heappop(negList)
            y = heapq.heappop(negList)
            if x < y:
                val = x - y
                heapq.heappush(negList, val)
            # if x < y then x == y beacuse of heap structure
        if len(negList) == 0:
            return 0
        else:
            return -(negList[0])
