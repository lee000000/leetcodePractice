'''
Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
class Solution(object):
    def reverseString(self, s):
        '''
        :type s: str
        :rtype: str
        '''
         
        if len(s) == 1 or len(s) == 0:
            return s
        if len(s) == 2:
            return (s[1]+s[0])
        s = list(s)
        start = 0
        end = len(s) - 1
        while start <= end:
            def swap(s, start, end):
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                return s
            s = swap(s, start, end)
            start += 1
            end -= 1
        return ''.join(s) 
        
        
if __name__ == "__main__":
    test = Solution()
    print test.reverseString("123456789") 
     
