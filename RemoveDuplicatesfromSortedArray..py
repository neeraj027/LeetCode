class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=0
        seen=set()
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[index]=nums[i]
                index+=1
        return index