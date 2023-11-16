class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr=int(''.join(map(str,digits)))
        arr+=1
        lst=[int(num) for num in str(arr)]
        return lst