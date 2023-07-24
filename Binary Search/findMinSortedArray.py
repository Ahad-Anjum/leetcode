class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        result = nums[0]
        while(l <= r):
            mid = (l + r)//2
            result = min(result, nums[mid])
            if (nums[mid] > nums[r]):
                l = mid + 1
            else: 
                r = mid - 1

        return min(result, nums[l])
    