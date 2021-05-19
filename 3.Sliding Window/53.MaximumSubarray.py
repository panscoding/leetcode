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
        window_start, window_sum, window_max= 0, 0, 0
        for i in range(len(nums)):
            window_sum += nums[i] #add the next element
            # slide the window, we don't need to slide if we have not hit the required window size of K
            if i >= k-1:
                # calculate the maximum sum
                if window_sum > window_max:
                    window_max = window_sum
                window_sum -= nums[window_start] #substract the element going out
                window_start += 1 #slide the window ahead
        return window_max

def main():
    a = Solution()
    result = a.findMaximumSubarraySlidingWindow(4, [-2,1,-3,4,-1,2,1,-5,4])
    print("(Sliding Window)Maximum of subarrays of size K: " + str(result))

if __name__ == "__main__":
    main()

