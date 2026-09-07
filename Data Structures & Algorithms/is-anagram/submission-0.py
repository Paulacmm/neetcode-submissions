class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))
        
        for index in range(len(s)):
            if s_sorted[index] != t_sorted[index]:
                return False
        
        return True
        