import math

class Solution:

    # linear time check for a specific k if it can finish the piles
    def canFinish(self, piles: List[int], h: int, k: int) -> bool:
        time_to_eat = 0
        for pile in piles:
            time_to_eat += math.ceil(pile / k)
            if time_to_eat > h:
                return False
        return True


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maximum = max(piles)

        if len(piles)==h:
            return maximum
        
        left = 1
        right = maximum
        last_k = (left+right)//2

        while left<=right:
            mid = (left+right)//2
            if not self.canFinish(piles, h, mid):
                left = mid+1
            elif self.canFinish(piles, h, mid):
                last_k = mid
                right = mid-1

        return last_k 

            
