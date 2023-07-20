class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
        while left <= right:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else: 
                left += 1
                right -= 1
        return -1
    #Better written solution
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else: 
                return mid
        return -1