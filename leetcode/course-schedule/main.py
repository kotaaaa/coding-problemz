class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graphs = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graphs[b].append(a)
        visited = [-1 for _ in range(numCourses)]
        for course in range(numCourses):
            if dfs(course, visited, graphs):
                return False
        return True


def dfs(course, visited, graphs):
    if visited[course] == 1:
        return True
    if visited[course] == 2:
        return False
    visited[course] = 1
    for j in graphs[course]:
        if dfs(j, visited, graphs):
            return True
    visited[course] = 2
    return False
