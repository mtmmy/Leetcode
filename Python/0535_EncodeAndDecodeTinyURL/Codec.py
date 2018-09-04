import string
import random
class Codec:

    def __init__(self):
        self.shortToLong = {}
        self.longToShort = {}

    def randomString(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        while True:
            randomUrl = self.randomString()
            if randomUrl not in self.shortToLong:
                self.shortToLong[randomUrl] = longUrl
                self.longToShort[longUrl] = randomUrl
                return randomUrl
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.shortToLong[shortUrl]