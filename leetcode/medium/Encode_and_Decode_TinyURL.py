import random
import string


class Codec:
    alphabet = string.ascii_letters + '123456789'
    hardUrl = 'https://posia.com/'

    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}

    def encode(self, longUrl):
        shortUrl = ''
        while longUrl not in self.url_to_code:
            code = ''.join(random.choice(Codec.alphabet) for _ in range(6))
            if code not in self.url_to_code:
                shortUrl = Codec.hardUrl + code
                self.url_to_code[longUrl] = code
                self.code_to_url[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl):
        return self.code_to_url[shortUrl]


codec = Codec()
shortUrl = codec.encode('https://leetcode.com/problems/design-tinyurl')
print(shortUrl)
print(codec.decode(shortUrl))
