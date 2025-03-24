class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        today = 0
        meetings.sort(key = lambda x : x[0])
        for beg, end in meetings:
            
            if end <= today: continue                  
            if beg <= today:  days-= end - today        
            else: days-= end - beg + 1                

            today = end
                
        return days                       