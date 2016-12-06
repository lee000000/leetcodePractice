'''
14. Longest Common Prefix

Write a function to find the longest common prefix

string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        if len(strs) == 1:
            return strs[0]

        common = strs[0]

        for s in strs:
            j = 0
            ret = []
            while j < len(s) and j < len(common):
                if s[j] == common[j]:
                    ret.append(common[j])
                else:
                    break
                j += 1
            common = "".join(ret)

        return common


if __name__ == "__main__":
    a = ["acb","ba"]
    sol = Solution()
    print(sol.longestCommonPrefix(a))
