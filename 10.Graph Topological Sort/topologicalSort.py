"""
Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

Given a directed graph, find the topological ordering of its vertices.

Example 1:

Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
Output: Following are the two valid topological sorts for the given graph:
1) 3, 2, 0, 1
2) 3, 2, 1, 0
"""
from collections import deque
class Solution:
    def topologicalSort(self,vertices, edges):
        """
        1. Solution:
        Topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for
        every directed edge uv from vertex u to vertex v, u comes before v in the ordering. F
        https://en.wikipedia.org/wiki/Topological_sorting

        2. Time Complexity

        3. Space Complexity

        :param vertices:
        :param edges:
        :return:
        """
        sortedOrder = []
        if vertices <= 0:
            return sortedOrder

        #1. init the in_degree of the child and  the graph
        inDegree = {i: 0 for i in range(vertices)} #in-degree save each node's in degree
        # print("inDegree: ", inDegree)
        graph = {i: [] for i in range(vertices)} # graph, key: value, key is the node. value is list of all child
        # print("graph: ", graph)

        #2. build the graph and inDegree
        for edge in edges:
            parent, child = edge[0], edge[1]
            graph[parent].append(child) # the graph's value append the child
            inDegree[child] += 1 # increase the in degree of each child by one

        #3. find the source
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        #4 iterate the source and popup it
        # iterate the child of vertex, decrement the in-degree of each child by 1
        # if the child's in-degree equal to zero, push to source.
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            #decrement the indegree
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)

        if vertices != len(sortedOrder): #has cycle
            return []

        return sortedOrder

def main():
    a = Solution()
    print("Topological sort: " +
        str(a.topologicalSort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(a.topologicalSort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(a.topologicalSort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

if __name__ == "__main__":
    main()