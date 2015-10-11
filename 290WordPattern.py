'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a substring in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(pattern)!= len(str_list):
            return False
        mapping = {}
        mapped_str = []
        for i in xrange(len(pattern)):
            key = pattern[i]
            if not mapping.has_key(key):
                mapping[key] = str_list[i]
                #multiple keys should not mapping to the same str
                if str_list[i] in mapped_str:
                    return False
                mapped_str.append(str_list[i])
            else:
                if str_list[i]!= mapping[key]:
                    return False     
        return True
        
if __name__ == '__main__':
    s = Solution()
    pattern = 'abba'
    str = "dog dog dog dog"
    print s.wordPattern(pattern, str)