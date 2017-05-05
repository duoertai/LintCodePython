class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        res = []
        if nestedList is None:
            return res

        if type(nestedList) is not list:
            res.append(nestedList)
            return res

        for temp in nestedList:
            if type(temp) is list:
                lst = self.flatten(temp)
                res.extend(lst)
            else:
                res.append(temp)

        return res
