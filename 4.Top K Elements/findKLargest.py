"""

"""
from heapq import *

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

    def distance_from_origin(self):
        return self.x * self.x + self.y * self.y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()


class Solution:
    def kClosest(self, points, k: int):
        max_heap = []
        for i in range(k):
            heappush(max_heap, points[i])
        print(max_heap)

        for j in range(k, len(points)):
            if points[j].distance_from_origin() < max_heap[0].distance_from_origin():
                heappop(max_heap)
                heappush(max_heap, points[j])

        return list(max_heap)




def main():
    a = Solution()
    result = a.kClosest([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()

if __name__ == "__main__":
    main()
