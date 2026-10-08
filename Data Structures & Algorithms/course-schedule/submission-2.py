
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [0,1] [1, 2] [2, 3] [3, 0]
           
        # create our tree
        courses = defaultdict(list)  # course -> its future classes. 

        for before, after in prerequisites:
            courses[before].append(after)


        # dfs through the tree:
        preSet = set()

        def dfs(start):
            if start in preSet:
                return False
            if courses[start] == []:
                return True

            preSet.add(start)

            for c in courses[start]:
                if not dfs(c):
                    return False

            preSet.remove(start)
            courses[start] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True






