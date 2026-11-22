class Solution:
    def checkString(self, s: str) -> bool:
        for right in range(len(s)-1):
            if s[right]=='b' and s[right+1]=='a':
                return False
        return True

      
        