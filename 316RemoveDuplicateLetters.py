'''
Given a string which contains only lowercase letters, remove duplicate letters so that every letter appear once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example:
Given "bcabc"
Return "abc"

Given "cbacdcbc"
Return "acdb"


Created on Feb 12, 2016

@author: Dahu
'''

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if s is None:
            return None
        
        counter = [0 for i in xrange(26)]
        for c in s:
            k = ord(c) - ord('a')
            counter[k] += 1
            
        stack = []
        visited = [False for i in xrange(26)]
        for c in s:
            k = ord(c) - ord('a')
            counter[k] -= 1
            if visited[k] is True:
                continue
            
            while stack and ord(stack[-1]) > ord(c) and counter[ord(stack[-1]) - ord('a')] > 0:
                visited[ord(stack.pop()) - ord('a')] = False
            
            stack.append(c)
            visited[k] = True
#            if c not in stack:
#                stack.append(c)
#            else:
#                for i in xrange(len(stack) - 1):
#                    if stack[i] == c:
#                        #check the next one's order
#                        nc = stack[i+1]
#                        if ord(nc) < ord(c):
#                            stack.remove(c)
#                            stack.append(c)
        return "".join(stack)
        
if __name__ == '__main__':
    tt = "cbacdcbc"
    s = Solution()
    print s.removeDuplicateLetters(tt)