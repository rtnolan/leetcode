#two_sum.py
class Solution:
    """LeetCode twoSum question"""
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers such that they add up to a specific target.
        Args:
            nums: list[int] -- list of numbers
            target: int -- target number
        Return:
            list[int] -- indices of numbers which sum to target.
        """
        res = {}
        for k, val in enumerate(nums):
            if val in res:
                return [res[val], k]
            res[target-val] = k
