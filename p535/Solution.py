import random


class Codec:
    def __init__(self):
        self.mapDict = {}
        self.charSet = []
        for i in range(26):
            self.charSet.append(chr(i + ord('a')))
            self.charSet.append(chr(i + ord('A')))
        for i in range(10):
            self.charSet.append(chr(i + ord('0')))

    def randomString(self):
        hash = ''
        for i in range(7):
            hash += self.charSet[random.randint(0, 35)]
        return hash

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        hash = self.randomString()
        self.mapDict[hash] = longUrl
        return 'http://tinyurl.com/' + hash

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.mapDict[shortUrl[19:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
