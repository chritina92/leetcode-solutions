
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])

        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)
