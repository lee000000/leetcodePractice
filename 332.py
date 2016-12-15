'''
Given a list of airline tickets represented by pairs of departure and arrival

airports [from, to], reconstruct the itinerary in order. All of the tickets belong

to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has

the smallest lexical order when read as a single string. For example, the itinerary

["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]

Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].

But it is larger in lexical order.
'''
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # iteratively look for starting vertex ["JFK", "XXX"]
        # DFS entire array for an acylic path
        if tickets == []:
            return []

        target = "JFK"
        ret = []
        for item in tickets:
            if item[0] == "JFK":
                if ret == []:
                    ret.append(item)
                else:
                    if ret[0][1] > item[1]:
                        ret.pop()
                        ret.append(item)

        i = tickets.index(ret[0])
        # break at target and search new target at the reconnected array
        # without the previous target
        newT = tickets[0:i] + tickets[i + 1:]

        return list(set(self.helper(tickets, newT, ret, 0)))

    def helper(self, tickets, newT, ret, count):
        count += 1
        if count >= 20:
            return 0
        if len(newT) == 0:
            return ret

        lNewRet = len(tickets) - len(newT)

        target = ret[lNewRet-1][1]
        # print(target)

        for item in newT:
            if item[0] == target:
                if len(ret) < lNewRet + 1:
                    ret.append(item)
                else:
                    if ret[1][1] > item[1]:
                        ret.append(item)

        # print(ret)
        # print(lNewRet)
        i = newT.index(ret[lNewRet])
        newT = newT[0:i] + newT[i+1:]
        return self.helper(tickets, newT, ret, count)


def test():
    t = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    sol = Solution()
    print(sol.findItinerary(t))


if __name__ == "__main__":
    test()
