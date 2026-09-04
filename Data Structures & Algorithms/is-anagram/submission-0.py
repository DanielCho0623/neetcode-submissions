class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        seen_b = dict()
        for char in s:
            seen[char] = seen.get(char,0) +1 
        for j in t:
            seen_b[j] = seen_b.get(j, 0) + 1
        if seen == seen_b:
            return True
        return False
        
        