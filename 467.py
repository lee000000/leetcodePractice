'''
467. Unique Substrings in Wraparound String

Consider the string s to be the infinite wraparound string of

"abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique

non-empty substrings of p are present in s. In particular, your input is

the string p and you need to output the number of different non-empty

substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p

might be over 10000.

Example 1:
Input: "a"
Output: 1
Explanation: Only the substring "a" of string "a" is in the string s.

Example 2:
Input: "cac"
Output: 2
Explanation: There are two substrings "a", "c" of string "cac" in the string s.

Example 3:
Input: "zab"
Output: 6
Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
string "zab" in the string s.
False Trial:
1. subproblems
    - the next non-consecutive character i0...ik,
2. guessing a possible solution
    - G(ik) = sum[ik - i0, ..., 1]
    - G(p) = sum(G(i))
3. recurrences:
    - G(p) = sum(sum(ik - i0,...1))
4. time: O(n * S) S is the length of each possible substring of s

Correct Sol:
1. subproblems:
    - unique substring ending with 'a', 'b', 'c',...'z'
2. guess a sol:
    - F('a') = len(unique substring) - 1
    - Count(n) = F('a') + F('b') +...+F('z')
'''
class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        dp = [0] * 26
        length_at_chr = 0
        for i in range(len(p)):
            if (i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1
            or abs(ord(p[i]) - ord(p[i - 1])) == 25)):
                length_at_chr += 1
            else:
                length_at_chr = 1

            index = ord(p[i]) - ord('a')
            if length_at_chr > dp[index]:
                dp[index] = length_at_chr
        #print(dp)



        return sum(dp)

    #     G = [0] * (len(p) + 1)
    #     G[0] = 1
    #     i = 1
    #     while i < (len(p)):
    #         j = i - 1
    #
    #         while (ord(p[i]) - ord(p[j]) != 1) or (p[i] == "a" and p[j] != "z") or (p[i] != "a" and p[j] == "z") and i < len(p):
    #             G[i] = 1
    #             i += 1
    #             j += 1
    #
    #         while i < len(p) and ((ord(p[i]) - ord(p[j]) == 1) or (p[i] == "a" and p[j] == "z") or (p[i] == "a" and p[j] == "z")):
    #
    #             i += 1
    #         print(G)
    #         print(i)
    #         G[i] = self.sumSub(j, i)
    #
    #     return sum(G[0:-2])
    #
    # def sumSub(self, j, i):
    #     sum = 0
    #     for k in range(i - j):
    #         sum += k
    #     print(sum)

def test():
    p = "zababcdeabcaipfhi"
    sol = Solution()
    print(sol.findSubstringInWraproundString(p))


if __name__ == "__main__":
    test()
