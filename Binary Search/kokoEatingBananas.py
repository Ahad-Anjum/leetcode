class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
         # minimum for 5 will be size of piles, n
        left, right = 0, max(piles)
        res = max(piles)

        while left <= right:
            k = (left + right )//2
             
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)

            if totalTime <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1
        return res