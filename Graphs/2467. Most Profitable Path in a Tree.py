class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:

        def dfs_bob(node, parent, time):
            if node == 0:
                reach_time[node] = time
                return True
            for neighbor in graph[node]:
                if neighbor != parent and dfs_bob(neighbor, node, time+1):
                    reach_time[node] = time
                    return True
            return False

        def dfs_alice(node, parent, time):  
            income = -inf
            for neighbor in graph[node]:
                if neighbor != parent:
                    income = max(dfs_alice(neighbor, node, time+1), income)
            if income == -inf:  # Current node is a leaf
                income = 0
            if time < reach_time[node]:
                return income + amount[node] 
            if time == reach_time[node]:
                return income + amount[node] // 2
            return income

        graph = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
           graph[u].append(v)
           graph[v].append(u)
        reach_time = [inf]*(len(edges)+1)
        dfs_bob(bob, -1, 0)
        return dfs_alice(0, -1, 0)