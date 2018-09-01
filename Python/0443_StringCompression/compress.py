class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # left = i = 0
        # while i < len(chars):
        #     char, length = chars[i], 1
        #     while (i + 1) < len(chars) and char == chars[i + 1]:
        #         length, i = length + 1, i + 1
        #     chars[left] = char
        #     if length > 1:
        #         len_str = str(length)
        #         chars[left + 1:left + 1 + len(len_str)] = len_str
        #         left += len(len_str)
        #     left, i = left + 1, i + 1
        # return left
        if not chars:
            return ""
        counter = 1
        i, j = 0, 1
        
        while j < len(chars):
            if chars[i] == chars[j]:
                counter += 1
                j += 1
            else:
                if counter > 1:
                    counterChars = list(str(counter))
                    chars[i + 1:j] = counterChars
                    j -= counter - 2 + len(counterChars) - 1
                    counter = 1
                    i = j + len(counterChars) - 1
                    j += 1 + len(counterChars) - 1
                else:
                    i += 1
                    j += 1
            
            
        if counter != 1:
            chars[i + 1:] = list(str(counter))

        print(chars)
        return len(chars)
                
        