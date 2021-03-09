"""
iven an unsorted array of numbers, find Kth smallest number in it.

Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

Example 1:

Input: [1, 5, 12, 2, 11, 5], K = 3
Output: 5
Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].
"""
from heapq import *

class Solution:
    def findKthSmallest(self, nums, k: int) -> int:
        """
        implement the max_heap use push -nums[i] to the heap
        1. Solution:
        THis solution use the maximum heap which root is the biggest element in the max heap.
        Since we want track of the K smallest numbers, we can compare each number with the root while iterating throught all numbers.
        If it is smaller than root, we will take out the root and insert the smaller number.

        2. Time Complexity
        The time complexity of readjust the heap is O(Log(N)) where N is element of input nums. The heap is a binary tree,
        each time insert a new element, the tree rebalance will cost O(Log(N)). The time complexity of this solution is O(N*Log(N))
        where N is the element of nums.

        3. Space Complexity
        The algorithm runs in constant space O(1)
        The space complexity will be O(K) bacause we ned to store K smallest numbers in the heap

        :param nums:
        :param k:
        :return:
        """
        max_heap = []
        #1. insert first k number into the maximum heap.
        for i in range(k):
            heappush(max_heap, -nums[i])

        #2. Go throught the rest of number, if the current number smaller than the root, take out the root and push the current number.
        for j in range(k, len(nums)):
            if nums[j] < -max_heap[0]:
                heappop(max_heap)
                heappush(max_heap, -nums[j])

        #3. return the root as Kth element.
        return -max_heap[0]



def main():
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    a = Solution()
    ret = a.findKthSmallest(nums, k)
    print(ret)

if __name__ == "__main__":
    main()