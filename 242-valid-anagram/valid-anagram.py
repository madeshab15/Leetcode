class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        rs={}
        rt={}
        for i in range(len(s)):
            rs[s[i]]=rs.get(s[i],0)+1
        for i in range(len(t)):
            rt[t[i]]=rt.get(t[i],0)+1
        return rs == rt


        