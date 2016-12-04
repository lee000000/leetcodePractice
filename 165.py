'''
165. Compare Version Numbers

Compare two version numbers version1 and version2.

If version1 > version2 return 1, if version1 < version2

return -1, otherwise return 0.

You may assume that the version strings are non-empty and

contain only digits and the . character.

The . character does not represent a decimal point and is

used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to

version three", it is the fifth second-level revision of the

second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")

        d = len(v2) - len(v1)

        v1 += [0] * d
        v2 += [0] * -d

        for i in range(len(v1)):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                continue
        return 0

    def fasterSolution(self, version1, version2):
        v1, v2 = (map(int, v.split('.')) for v in (version1, version2))
        d = len(v2) - len(v1)
        return cmp(v1 + [0]*d, v2 + [0]*-d)

if __name__ == "__main__":
    v = ["01",\
        "1"]

    sol = Solution()
    print(sol.compareVersion(v[0], v[1]))
