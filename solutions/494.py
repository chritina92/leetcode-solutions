
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        if (target+total_sum) % 2 == 1:
            return 0
        target_sum = (target+total_sum) //2
        dp = [[0] * (target_sum + 1) for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(target_sum+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1]:
                    dp[i][j] += dp[i-1][j-nums[i-1]]

        return dp[len(nums)][target_sum]
# leetcode submit region end(Prohibit modification and deletion)
