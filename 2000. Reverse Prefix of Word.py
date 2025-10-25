class Solution(object):
    def reversePrefix(self, word, ch):
        i=word.find(ch)
        if not i:
            return word
        return word[:i+1][::-1]+word[i+1:]
        
