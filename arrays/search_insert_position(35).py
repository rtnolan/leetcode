class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try:
            i = nums.index(target)
            return i
        except:
            for i in range(0, len(nums)):
                if target < nums[i]:
                    return i
            return len(nums)
