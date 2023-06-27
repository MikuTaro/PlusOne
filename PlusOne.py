class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        self.num = int(''.join(map(str, digits))) + 1
        self.num = [int(x) for x in str(self.num)]

ans = Solution()
ans.plusOne([9])
print(ans.num)