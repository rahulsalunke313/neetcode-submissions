class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxx = max(piles)
        minn = 1

        while minn <= maxx:
            mid = (minn + maxx) // 2
            print(minn,mid,maxx)
            total = sum([math.ceil(x/mid) for x in piles])
            print(mid,total)
            if total <= h:
                maxx = mid - 1
            else:
                minn = mid + 1
        return minn
