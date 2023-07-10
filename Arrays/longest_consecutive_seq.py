class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0

        for num in nums:
            if(num -1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                count = max(count, length)
        return count