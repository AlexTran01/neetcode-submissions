
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0,1] [1, 2] [2, 3] [3, 0]
           
        # create our tree
        courses = defaultdict(list)  # course -> its future classes. 

        for before, after in prerequisites:
            courses[before].append(after)

        # dfs through the tree:
        preSet = set()
        def dfs(node):
            if courses[node] == []:
                return True
            if node in preSet:
                return False

            preSet.add(node)

            for c in courses[node]:
                if not dfs(c):
                    return False

            # preSet.remove(node)
            courses[node] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True






