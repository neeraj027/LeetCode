class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        temp=[]
        i=0
        while i<n1 or i<n2:
            if i<n1:
                temp.append(word1[i])
            if i<n2:
                temp.append(word2[i])
            i+=1
        return ''.join(temp)