'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.

Created on Feb 12, 2016

@author: Dahu
'''

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if words is None:
            return 0
        
        bit_value = [0 for i in xrange(len(words))]
        i = 0
        for w in words:
            for c in w:
                bit_value[i] |= 1 << ord(c) - ord('a')
            i = i + 1
            
        res = 0
        for i in xrange(len(words)):
            for j in xrange(i+1, len(words)):
                if (bit_value[i] & bit_value[j]) == 0 and len(words[i]) * len(words[j]) > res:
                    res = len(words[i]) * len(words[j])
        return res
        
#        for i in xrange(len(words)):
#            word_map = {}
#            for c in words[i]:
#                word_map[c] = True
#            len_s = len(words[i])
#            
#            for word in words[i+1:]:
#                share = False
#                for w in word:
#                    if word_map.has_key(w):
#                        share = True
#                        break
#                if not share and len_s * len(word) > res:
#                    res = len_s * len(word)
#        return res
        
if __name__ == '__main__':
    s = Solution()
    words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#    words = ["a", "aa", "aaa", "aaaa"]
    print s.maxProduct(words)
