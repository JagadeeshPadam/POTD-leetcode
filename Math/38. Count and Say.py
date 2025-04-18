class Solution:
    def countAndSay(self, n: int) -> str:
        num = '1'
        
        for _ in range(1, n):
            next_num = ''
            count = 1
            
            for j in range(1, len(num)):
                if num[j] == num[j - 1]:
                    count += 1
                else:
                    next_num += str(count) + num[j - 1]
                    count = 1
            
            next_num += str(count) + num[-1]
            num = next_num
        return num