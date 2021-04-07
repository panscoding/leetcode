"""
In many problems dealing with an array (or a LinkedList), we are asked to find or calculate something among all the contiguous subarrays (or sublists) of a given size. For example, take a look at this problem:

Given an array, find the average of all contiguous subarrays of size ‘K’ in it.
Let’s understand this problem with a real input:

Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:
"""

class Solution:
    def findAveragesofSubarraysBruteForce(self, K, arr):
        result = []
        _sum = 0

        for i in range(len(arr) - K + 1):
            _sum = 0
            for j in range(i, i+K):
                _sum += arr[j]
            result.append(_sum/K)
        return result
    def findAveragesofSubarraysSlidingWindow(self, K, arr):
        result = []
        window_size = 0
        window_start = 0
        _sum_window = 0
        for i in range(len(arr)):
            _sum_window += arr[i]
            window_size += 1
            if window_size == K:
                result.append(_sum_window/K)
                _sum_window -= arr[window_start]
                window_size -= 1
                window_start += 1
        return result

    def findAveragesofSubarraysSlidingWindowGood(self, K, arr):
        result = []
        window_start = 0
        window_end = 0
        _sum_window = 0
        for window_end in range(len(arr)):
            _sum_window += arr[window_end] #add the next element
            #slide the window, we don't need to slide if we have not hit the required window size of K
            if window_end >= K -1:
                result.append(_sum_window/K) #calculate the average
                _sum_window -= arr[window_start] #subtract the element going out
                window_start += 1 #slide the window ahead
        return result

def main():
    a = Solution()
    result = a.findAveragesofSubarraysBruteForce(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("(Brute Force)Averages of subarrays of size K: " + str(result))
    result = a.findAveragesofSubarraysSlidingWindow(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("(Sliding Window)Averages of subarrays of size K: " + str(result))
    result = a.findAveragesofSubarraysSlidingWindowGood(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("(Sliding Window)Averages of subarrays of size K: " + str(result))

if __name__ == "__main__":
    main()
