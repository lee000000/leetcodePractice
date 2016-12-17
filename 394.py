'''
394. Decode String

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string

inside the square brackets is being repeated exactly k times. Note

that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white

spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain

any digits and that digits are only for those repeat numbers, k. For

example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        mul = ""

        stack = [["", 1]]

        for l in s:
            if l.isdigit():
                mul += l
            elif l == "]":
                ch, n = stack.pop()

                stack[-1][0] += ch * n
                print("here1", stack)
            elif l == "[":
                stack.append(["", int(mul)])
                mul = ""
                print("here2", stack)
            else:
                # extend substring to be repeated
                stack[-1][0] += l
                print("here3", stack)

            # print(stack)
            # print(mul)
            return stack[0][0]


        # stack = []
        # stack.append(["", 1])
        # num = ""
        # for ch in s:
        #     if ch.isdigit():
        #       num += ch
        #     elif ch == '[':
        #         stack.append(["", int(num)])
        #         num = ""
        #         print("here1", stack)
        #     elif ch == ']':
        #         st, k = stack.pop()
        #         stack[-1][0] += st*k
        #         print("here2", stack)
        #     else:
        #         stack[-1][0] += ch
        #         print("here3", stack)

        return stack[0][0]


def test():
    s = s = "3[a2[c]]"
    sol = Solution()
    sol.decodeString(s)


if __name__ == "__main__":
    test()
