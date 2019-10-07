class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
          type: nums1 : List[int]
          type: m : int
          type: nums2 : List[int]
          type: n : int
          rtype: None
        """
        nums1[m:] = nums2[:n]
        nums1.sort()
  
