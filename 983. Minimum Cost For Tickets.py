class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        def fun(i):
            if i >= n:
                return 0
            
            cost0 = costs[0] + fun(i + 1)
            
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            cost1 = costs[1] + fun(j)
            
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            cost2 = costs[2] + fun(j)
            
            return min(cost0, cost1, cost2)
        
        return fun(0)
