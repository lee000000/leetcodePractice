'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern

on a given number of rows like this: (you may want to display

this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

P    I    N
A  L S  I G
Y A  H R
P    I
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion

given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if s == "" or len(s) <= numRows or numRows == 1:
            return s

        ret = []
        row = 0
        while row < numRows:
            ret.append(list())
            row += 1

        flag = numRows - 1
        row = 0
        for l in s:
            print(ret)
            ret[abs(row)].append(l)
            # Going from Top -> Bottom
            if (row > 0) and (row == flag):
                    flag = 0
                    row = -row + 1
                    continue
            # Going from Bottom -> Top
            if (row <= 0) and (row == flag):
                    flag = numRows - 1
                    row += 1
                    continue
            row += 1


        retS = "".join(map("".join, ret))
        return retS



if __name__ == "__main__":
    b = "ab"
    a = "PAYPALISHIRING"
    sol = Solution()
    print(sol.convert(b, 1))
