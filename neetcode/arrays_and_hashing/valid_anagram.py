def isAnagram( s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        
        s_map = {}
        t_map = {}
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
        for i in range(len(t)):
            t_map[t[i]] = 1 + t_map.get(t[i], 0)

        return s_map == t_map
            



print(isAnagram('anagram', 'nagaram')) #True
print(isAnagram('rat', 'car')) # False