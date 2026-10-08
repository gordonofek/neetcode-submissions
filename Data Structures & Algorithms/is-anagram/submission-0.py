class Solution:
    def isAnagram(self, s: str, t: str) -> bool:#
        dict1 = {}
        dict2 = {}
        for c1 in s:
            dict1[c1] = dict1.get(c1, 0) + 1
        for c2 in t:
            dict2[c2] = dict2.get(c2, 0) + 1
        if(dict1 == dict2):
            return True
        else:
            return False
        