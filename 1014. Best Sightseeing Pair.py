# Question: Best Sightseeing Pair
# You are given an integer array values where values[i] represents the value of the ith 
# sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: 
# the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

# Intution:
# Running 2 loops and finding -> gives TLE 
# Hence, find maximum so far and then calculate the score
# Here need to calculate maximum of values[i] + values[j] - (j - i)
# So, we can calculate maximum of values[i] + i and then add values[j] - j to it

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        ans = -1
        maxsofar = values[0] + 0 # Keep undating this
        for i in range(1, n):  
            maxsofar = max(maxsofar, values[i-1]+i-1) 
            ans = max(ans, values[i] - i + maxsofar) # Calculate the score
        return ans