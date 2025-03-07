class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve(n):
            primes = [True] * (n + 1)
            primes[0], primes[1] = False, False

            for i in range(2, int(n ** 0.5) + 1):
                if primes[i]:
                    for j in range(i * i, n + 1, i):
                        primes[j] = False

            return primes

        N = 10**6
        t = sieve(N)
        nums = []
        for i in range(left, right+1):
            if t[i]:
                nums.append(i)
        mini = float('inf')
        ans = [-1, -1]
        for i in range(len(nums)-1):
            if mini > (nums[i+1] - nums[i]):
                mini = nums[i+1] - nums[i]
                ans = [nums[i], nums[i+1]]
        return ans