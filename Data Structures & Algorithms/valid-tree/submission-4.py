class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        chil_map = {i:[] for i in range(n)}

        for node1, node2 in edges:
            chil_map[node1].append(node2)
            chil_map[node2].append(node1)


        
        visited = set()

        def dfs(cur, prev):

            if cur in visited:
                return False
            

            visited.add(cur)

            for chil in chil_map[cur]:
                if chil == prev:
                    continue
                if not dfs(chil, cur):
                    return False
            
    
            #chil_map[cur] = []
            return True

        
        if not dfs(0,-1):
            return False
        
        return len(visited) == n 

        