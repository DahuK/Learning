
#All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 
#When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
#Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
#For example,
#
#Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
#
#Return:
#["AAAAACCCCC", "CCCCCAAAAA"].

class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        length = len(s)
        repeat_list = []
        if length < 11:
            return repeat_list
        ss_map = {}
        for x in xrange(len(s)):
            ss = s[x: x+10]
            key = self.generate_key(ss)
            if key == None:
                return repeat_list
            if ss_map.get(key) == None:
                ss_map[key] = 1
            elif ss_map.get(key) == 1:
                repeat_list.append(ss)                
                ss_map[key] = 2            
        return repeat_list
        
    
    def generate_key(self, ss):
        last_na = ss[0]
        count = 0
        key = ''
        length = len(ss)
        if not length == 10:
            return None
        for c in ss:
            if c == last_na:
                count += 1
            else:
                key += last_na + str(count)
                count = 1
                last_na = c
        key += last_na + str(count) 
        return key
        
if __name__ == '__main__':
    ss_map = {}
    key = 'sad'
    if ss_map.get(key) == 1:
        print 'aaa'  
    test = 'AAAAGGGTTT'
#    for c in s:
#        print c
#    print len(s)
#    key = ''
#    count = 4
#    key += 'A' + str(count)
#    print key
    s = Solution()
    ss = s.generate_key(test)
    print ss
    ss = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    rl = s.findRepeatedDnaSequences(ss)
    print rl

