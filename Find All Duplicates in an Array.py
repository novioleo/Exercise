# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [2,3]
# Union Find
class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        to_return = []
        for m_num in nums:
            m_num *= -1 if m_num < 0 else 1
            nums[m_num-1] *= -1
            if nums[m_num-1] > 0:
                to_return.append(m_num)
        return to_return

if __name__ == '__main__':
    s = Solution()
    print(s.findDuplicates([4,3,2,7,8,2,3,1]))