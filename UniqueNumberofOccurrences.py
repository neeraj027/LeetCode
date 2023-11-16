class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict1={}
        lst=[]
        for i in arr:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in dict1.keys():
            lst.append(dict1[i])
        if len(lst)==len(set(lst)):
            return True
        return False