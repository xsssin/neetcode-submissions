class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        gmap = {i:[] for i in range(n)}


        for node1, node2 in edges:
            gmap[node1].append(node2)
            gmap[node2].append(node1)
        count = 0
        visited = set()
        def dfs(cur,prev):
            if cur in visited:
                return False
            
            visited.add(cur)


            for chil in gmap[cur]:
                if chil == prev:
                    continue
                dfs(chil,cur)
                    
            

        
            return True

        
        for i in range(n):
            if i in visited:
                continue
            
            dfs(i,-1)
            count+=1

        return count

            
            

        