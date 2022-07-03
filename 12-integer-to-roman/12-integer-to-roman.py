class Solution:
    def intToRoman(self, num: int) -> str:
        res=""
        roman = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        for m in dict(reversed(list(roman.items()))):
            if num//roman[m]:
                count = num//roman[m]
                res += m*count
                num = num % roman[m]
        return res
                
        