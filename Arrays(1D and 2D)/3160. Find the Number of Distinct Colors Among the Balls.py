class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hmap = {}
        color = defaultdict(int)
        ptr = 0
        ans = []
        
        for p, q in queries:
            if p in hmap:
                prev_value = hmap[p]
                color[prev_value] -= 1
                if color[prev_value] == 0:
                    color.pop(prev_value)
            hmap[p] = q
            color[q] += 1
            ans.append(len(color))

        return ans