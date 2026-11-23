class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        count1=Counter(t)
        count={}
        left=0
        required=len(count1)
        formed=0
        min_len=float('inf')
        result =""
        for right in range(len(s)):
            char=s[right]
            count[char]=count.get(char,0)+1
            if char in count1 and count[char]==count1[char]:
                formed+=1
            while formed==required:
                if right-left+1<min_len:
                    min_len=right-left+1
                    result=s[left:right+1]
                left_char=s[left]
                count[left_char]-=1
                if left_char in count1 and count[left_char]<count1[left_char]:
                    formed-=1
                left+=1
        return result

       