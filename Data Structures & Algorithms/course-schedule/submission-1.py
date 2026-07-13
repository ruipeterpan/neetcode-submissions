class Node:
    def __init__(self, course_id: int):
        self.course_id = course_id
        self.prerequisites = []  # list of pointers

class Solution:
    

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [Node(i) for i in range(numCourses)]

        # graph: each node is a class.
        # if there is a cycle: return false.
        for course, prereq in prerequisites:
            courses[course].prerequisites.append(courses[prereq])
        
        visited = set()
        visiting = set()
        
        for course_id in range(numCourses):
            start = courses[course_id]
            
            def dfs(node):
                # returns True if, starting from this node, there are no cycles.
                # returns False if otherwise.
                if node.course_id in visiting:
                    return False
                if node.course_id in visited:
                    return True
                
                visiting.add(node.course_id)
                
                for prereq in node.prerequisites:
                    if not dfs(prereq):
                        return False

                visited.add(node.course_id)
                visiting.remove(node.course_id)
                
                return True
            
            if not dfs(start):
                return False
        return True




