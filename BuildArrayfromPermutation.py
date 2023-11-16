class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result=[]
        temp=0
        for i in range(len(nums)):
            temp=nums[i]
            result.append(nums[temp])
        return result