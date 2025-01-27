class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}
        for ps, cs in prerequisites:
            adj[cs] = adj.get(cs, []) + [ps]
        
        def dfs(crs):
            if crs not in pmap:
                pmap[crs] = set()
                for p in adj.get(crs, ()):
                    pmap[crs] |= dfs(p)
                pmap[crs].add(crs)

            return pmap[crs]

        pmap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        ans = []
        for u, v in queries:
            ans.append(u in pmap[v])
        return ans