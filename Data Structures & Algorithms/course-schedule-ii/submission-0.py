class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for cur,pre in prerequisites:
            preMap[cur].append(pre)

        visited = set()
        completed = set()
        res = []

        def dfs(cur):
        
                #basecae1:
                if cur in visited:
                    return False

                if cur in completed:
                    return True
            

                visited.add(cur)
                

                for pre in preMap[cur]:
                    if not dfs(pre): return False

                visited.remove(cur)
                completed.add(cur)
                res.append(cur)

                return True

        
        for cur in range(numCourses):
            if cur not in completed:
                if not dfs(cur):
                    return []
        
        return res
        






        