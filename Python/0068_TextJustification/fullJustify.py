import unittest

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result, remainWidth = [""], maxWidth
        for w in words:            
            if remainWidth >= len(w):
                result[-1] += w + " "
                remainWidth -= len(w) + 1
            else:
                result[-1] = result[-1].strip(" ")
                result.append("")
                result[-1] += w + " "
                remainWidth = maxWidth - len(w) - 1
        
        for i in range(len(result) - 1):
            n = len(result[i])
            if n < maxWidth:
                words = result[i].split(" ")
                if len(words) > 1:
                    spaces = maxWidth - n + (len(words) - 1)
                    gap = spaces // (len(words) - 1)
                    remainder = spaces % (len(words) - 1)
                    temp = ""
                    for j in range(len(words)):
                        temp += words[j]
                        if spaces == 0:
                            break
                        temp += " " * gap
                        spaces -= gap
                        if j < remainder:
                            spaces -= 1
                            temp += " "
                    result[i] = temp
                else:
                    result[i] = result[i] + " " * (maxWidth - len(result[i]))

        result[-1] = result[-1].strip(" ")
        if len(result[-1]) < maxWidth:
            result[-1] = result[-1] + " " * (maxWidth - len(result[-1]))
        
        return result
            


class TestFunc(unittest.TestCase):
    """Test fuction"""

    def test(self):
        target = Solution()
        expected = ["Science  is  what we","understand      well","enough to explain to","a  computer.  Art is","everything  else  we","do                  "]
        test = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        self.assertEqual(expected, target.fullJustify(test, 20))

        expected = ["This    is    an","example  of text","justification.  "]
        test = ["This", "is", "an", "example", "of", "text", "justification."]
        self.assertEqual(expected, target.fullJustify(test, 16))

        expected = ["What   must   be","acknowledgment  ","shall be        "]
        test = ["What","must","be","acknowledgment","shall","be"]
        self.assertEqual(expected, target.fullJustify(test, 16))

if __name__ == '__main__':
    unittest.main()
        