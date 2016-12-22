'''
91. Decode Ways


A message containing letters from A-Z is being encoded to numbers using the

following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of

 ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return 0

        # at least 2 characters in s
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for endi in range(1, len(s) + 1):
            # preCount, count = count, self.count(s[endi - 2 : endi]) + preCount + count

            if s[endi - 1] != "0":
                dp[endi] += dp[endi - 1]

            if endi != 1 and int(s[endi - 2:endi]) < 27 and  int(s[endi - 2:endi]) > 9:
                dp[endi] += dp[endi - 2]
        print(dp)
        return dp[-1]



def test():
    s = "110213"
    sol = Solution()
    print(sol.numDecodings(s))


if __name__ == "__main__":
    test()
