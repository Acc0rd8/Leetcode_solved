class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string_pattern = dict()
        s = s.split()
        
        if len(pattern) != len(s):
            return False
        
        for i in range(len(pattern)):
            if string_pattern.get(pattern[i]) is None:
                if s[i] in string_pattern.values():
                    return False
                else:
                    string_pattern[pattern[i]] = s[i]
            else:
                if string_pattern.get(pattern[i]) != s[i]:
                    return False
        
        return True
    
print(Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog"))