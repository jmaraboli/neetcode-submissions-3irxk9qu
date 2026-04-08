class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in s:
            if c not in t:
                return False
            count_s = s.count(c)
            count_t = t.count(c)
            if count_s != count_t:
                return False
        return True