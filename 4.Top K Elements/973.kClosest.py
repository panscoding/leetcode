"""
https://leetcode.com/problems/k-closest-points-to-origin/

"""
from heapq import *
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # used for max-heap
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        # ignoring sqrt to calculate the distance
        return (self.x * self.x) + (self.y * self.y)

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

class Solution:
    def kClosest(self, points, k: int):
        """
        1. Solution
        This problem follow the same solution with leetcode 215. We can use the minimum heap to keep the K minimum distance
        between zero and point. The root of mini heap is the smallest distance.
        2. Time Complexity
        The time complexity of this algorithm is (N∗logK) as we iterating all points and pushing them into the heap.
        3. Space Complexity
        The space complexity will be O(K) because we need to store ‘K’ point in the heap.
        :param points:
        :param k:
        :return:
        """
        maxHeap = []
        # put first 'k' points in the max heap
        for i in range(k):
            heappush(maxHeap, points[i])

        # go through the remaining points of the input array, if a point is closer to the origin than the top point
        # of the max-heap, remove the top point from heap and add the point from the input array
        for i in range(k, len(points)):
            if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
                heappop(maxHeap)
                heappush(maxHeap, points[i])

        # the heap has 'k' points closest to the origin, return them in a list
        return list(maxHeap)

def main():
    a = Solution()
    result = a.kClosest([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

if __name__ == "__main__":
    main()

