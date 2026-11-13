class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []
        res=[]
        need=Counter(p)
        window=Counter()
        k=len(p)
        for i in range(len(s)):
            window[s[i]]+=1
            if i>=k:
                left=s[i-k]
                window[left]-=1
                if window[left] == 0:
                    del window[left]
            if window==need:
                res.append(i-k+1)
        return res