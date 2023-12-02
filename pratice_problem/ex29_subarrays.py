class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxnumber = 0
        cursum = 0

        for i in nums:
            if cursum < 0 :
                cursum = 0
            cursum += i

            maxnumber = max(cursum,maxnumber)

        return maxnumber

