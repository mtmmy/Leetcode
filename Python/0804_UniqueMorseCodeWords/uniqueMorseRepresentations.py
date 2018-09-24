import string
class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = string.ascii_lowercase
        
        morseDict = dict(zip(alphabet, morseCode))
        
        result = set()
        
        for word in words:
            codedMorse = ""
            for c in word:
                codedMorse += morseDict[c]
            result.add(codedMorse)
        
        return len(result)