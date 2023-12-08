#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
          visit.add(n)
          n = sum(int(i) ** 2 for i in str(n))
          if n == 1:
            return True
        return False
# @lc code=end

