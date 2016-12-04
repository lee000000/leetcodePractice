'''
383. Ransom Note

Given an arbitrary ransom note string and another string

containing letters from all the magazines, write a function

that will return true if the ransom note can be constructed

from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
'''
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        # Use Hash
        dicm = {}
        dicr = {}
        for i in range(len(magazine)):
            if magazine[i] in dicm:
                dicm[magazine[i]] += 1
            else:
                dicm[magazine[i]] = 1

        for j in range(len(ransomNote)):
            if ransomNote[j] in dicr:
                dicr[ransomNote[j]] += 1
            else:
                dicr[ransomNote[j]] = 1

        for key in dicr.keys():
            if key not in dicm.keys():
                return False
            elif key in dicm.keys() and dicm[key] < dicr[key]:
                return False
            else:
                continue

        return True

if __name__ == "__main__":
    r = "bg"
    m = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    sol = Solution()
    print(sol.canConstruct(r, m))
    print("should be True")
