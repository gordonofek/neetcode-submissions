from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        
        for s in strs:
            array = [0] * 26
            for c in s:
                array[ord(c) - ord('a')] += 1
                
            map[tuple(array)].append(s)
            
        return list(map.values())