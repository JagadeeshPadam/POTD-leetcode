class Solution:
    def eventualSafeNodes(self, G):
        N = len(G)
        R = [[] for _ in range(N)]
        outdegree = [0] * N
        safe = [0] * N
        ans = []
        q = deque()
        
        for i in range(N):
            for v in G[i]:
                R[v].append(i)
            outdegree[i] = len(G[i])
            if outdegree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            safe[u] = 1
            for v in R[u]:
                outdegree[v] -= 1
                if outdegree[v] == 0:
                    q.append(v)
        
        for i in range(N):
            if safe[i]:
                ans.append(i)
        
        return ans
