class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(nums)):
            ans.append(nums[i])
            if i == len(nums)-1:
                for j in range(0,len(nums)):
                    ans.append(nums[j])
        return ans

nums = [1,2,1]
obj = Solution()
print(obj.getConcatenation(nums))