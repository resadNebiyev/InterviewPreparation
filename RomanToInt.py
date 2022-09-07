class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL': 40, 'XC':90, 'CD':400, 'CM':900} 
        result = 0
        x = 0
        while x < len(s): 
            if s[x: x + 2] in romans: 
                result += romans[s[x: x + 2]]
                x += 2 
            else:
                result += romans[s[x]]
                x += 1
        return result