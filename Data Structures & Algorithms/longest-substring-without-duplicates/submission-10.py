class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        
        l, curr, best = -1, 0, 0
        for r in range(len(s)):
            if s[r] not in dict:
                dict[s[r]] = r
            else:
                l = max(dict[s[r]], l)
                dict[s[r]] = r
            curr = r - l
            best = max(best, curr)

        return best