"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def findMaximumSubarraySlidingWindow(self, k, nums):
        """

        2. Time Complexity
            The time complexity of algorithm will be O(N)
        3. Space Complexity
            The algorithm runs in constant space O(1)

        """
        window_start, window_sum, window_max= 0, 0, 0
        for i in range(len(nums)):
            window_sum += nums[i] #add the next element
            # slide the window, we don't need to slide if we have not hit the required window size of K
            if i >= k-1:
                window_max = max(window_sum, window_max) # calculate the maximum sum
                window_sum -= nums[window_start] #substract the element going out
                window_start += 1 #slide the window ahead
        return window_max

    def findMaximumSubarrayBruteForce(self, k, nums):
        window_max = 0
        for i in range(len(nums)-k+1):
            window_sum = 0
            for j in range(i, i+k):
                window_sum += nums[j]
            window_max = max(window_sum, window_max)
        return window_max

def main():
    a = Solution()
    result = a.findMaximumSubarraySlidingWindow(4, [-2,1,-3,4,-1,2,1,-5,4])
    print("(Sliding Window)Maximum of subarrays of size K: " + str(result))

    result = a.findMaximumSubarrayBruteForce(4, [-2,1,-3,4,-1,2,1,-5,4])
    print("(Brute Force)Maximum of subarrays of size K: " + str(result))

if __name__ == "__main__":
    main()

