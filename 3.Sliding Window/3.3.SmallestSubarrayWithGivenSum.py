"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Problem Statement #
Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].

"""
import math

class Solution:
    def SmallestSubarrayWithGivenSumBurteForce(self, S, nums):
        for k in range(1, len(nums)+1):
        # each k size, calculate the sum
            window_start = 0
            window_sum = 0
            # print("k: ", k)
            for i in range(len(nums)-k+1):
                window_sum += nums[i] #add the next element
                # print("i: ", i)
                #slide the window, we don't need slide the window if we have not hit the required window size k
                if i >= k-1:
                    # print("window_sum: ", window_sum)
                    if window_sum >= S:
                        return k
                    window_sum -= nums[window_start] #substract the element going out
                    window_start += 1 #slide the window head
    def SmallestSubarrayWithGivenSumSlidingWindow(self, S, nums):
        """

        :param S:
        :param nums:
        :return:
        """
        min_length = math.inf
        window_start = 0
        window_sum = 0
        for window_end in range(len(nums)):
            window_sum += nums[window_end] #add the next element
            while window_sum >= S:
                min_length = min(window_end - window_start + 1, min_length) #record the minimum length
                #shrink the window_sum until it small than S
                window_sum -= nums[window_start]
                window_start += 1
        if min_length == math.inf:
            return 0
        return min_length

def main():
    a = Solution()
    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumBurteForce(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumBurteForce(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumBurteForce(8, [3, 4, 1, 1, 6])))

    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumSlidingWindow(7, [2, 1, 5, 2, 3, 2])))
    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumSlidingWindow(7, [2, 1, 5, 2, 8])))
    print("Smallest subarray length: " + str(a.SmallestSubarrayWithGivenSumSlidingWindow(8, [3, 4, 1, 1, 6])))


if __name__ == "__main__":
    main()