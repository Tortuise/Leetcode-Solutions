class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # logic sort one side by most expensive difference choose n most expensive differences for one side
        total = 0
        diff = {}
        for i in range(len(costs)):
            c = costs[i][0]-costs[i][1]
            diff[i] = c
        print(diff)
        indexes = sorted(diff, key=diff.get, reverse=True)
        i = 0
        while i < len(indexes):
            if i < len(indexes)/2:
                total += costs[indexes[i]][1]
            else:
                total += costs[indexes[i]][0]
            i += 1
        print(total)
        return total

