"""
1167 leetcode
https://leetcode.com/problems/minimum-cost-to-connect-sticks/
"""
from heapq import *
class Solutin:
    def minimumCostToConnectRopes(self, ropeLengths):
        mini_heap = []
        for i in range(len(ropeLengths)):
            heappush(mini_heap, ropeLengths[i])

        mini_value, temp, result = 0,0,0
        print("start", mini_heap)
        while len(mini_heap) > 1: # The last one is result, only need return the last one. Don't need add it up
            # print("----------")
            # print("working", mini_heap)
            mini_value = heappop(mini_heap)
            temp = mini_value + heappop(mini_heap)
            heappush(mini_heap, temp)
            result += temp
            # print("working-2", mini_heap)
        return result


def main():
    a = Solutin()
    print("Minimum cost to connect ropes: " +
          str(a.minimumCostToConnectRopes([1, 3, 11, 5])))
    # print("Minimum cost to connect ropes: " +
    #       str(a.minimumCostToConnectRopes([3, 4, 5, 6])))
    # print("Minimum cost to connect ropes: " +
    #       str(a.minimumCostToConnectRopes([1, 3, 11, 5, 2])))

main()