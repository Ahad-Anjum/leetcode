class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLen = 0
        left = 0
        charSet = set()
        for right in range(n):
            while(s[right] in charSet):
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            maxLen = max( maxLen, right - left + 1)

        return maxLen