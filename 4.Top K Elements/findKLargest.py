"""
Given an unsorted array of numbers, find the ‘K’ largest numbers in it.
Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.
Example 1:
Input: [3, 1, 5, 12, 2, 11], K = 3
Output: [5, 12, 11]
"""
from heapq import *

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        min_heap = []
        for i in range(k):
            heappush(min_heap, nums[i])

        for j in range(k, len(nums)):
            if nums[j] > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, nums[j])

        return list(min_heap)

def main():
    nums = [3,2,1,5,6,4]
    k = 3
    a = Solution()
    ret = a.findKthLargest(nums, k)
    print(ret)

if __name__ == "__main__":
    main()