"""
Problem Statement #
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.

Example 1:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: true
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish
before '2' can be scheduled. A possible sceduling of tasks is: [0, 1, 2]
Example 2:

Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: false
Explanation: The tasks have cyclic dependency, therefore they cannot be sceduled.
"""
from collections import deque
class Solution:
    def isSchedulingPossible(self, tasks, prerequisites):
        # TODO: Write your code here
        if tasks < 0:
            return False
        sortedOrder = []
        #1. define the in degree and graph
        inDegree = {i:0 for i in range(tasks)}
        graph = {i: [] for i in range(tasks)}

        #2. build the graph
        for prerequisite in prerequisites:
            parent, child = prerequisite[0], prerequisite[1]
            graph[parent].append(child)
            inDegree[child] += 1

        # 3. find the source
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        #4 intrate the source
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        if len(sortedOrder) == tasks:
            return True
        return False


def main():
    a = Solution()
    print("Is scheduling possible: " +
        str(a.isSchedulingPossible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(a.isSchedulingPossible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(a.isSchedulingPossible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

if __name__ == "__main__":
    main()
