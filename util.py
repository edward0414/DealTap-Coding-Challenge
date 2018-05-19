from random import randint 

class Converter:
    """
    A converter that generates a short url using the _id of the document in the db.
    Idea:
    - Every time a long url is received, an auto-incremented id will be assigned to that long url.
    - Then, with that id, use this converter to convert the number to a short string that represents 
    the short url.
    - Together, this id, the long url, and the short url will be saved into the db as a document.
    """

    _letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    _base = len(_letters)

    def convertToURL(self, num):
        #convert this 10-based number to 62-based number
        #then, use the letter to represent the 62-based number

        result = ''

        while num > 0:

            remain = num // self._base
            dig = num % self._base
            num = remain
            result = self._letters[dig] + result

        return result

    def convertToNum(self, url):
        #decode the url into a 62-based number
        #then, convert it back to 10-based number (the id in the db)

        num = 0

        for char in url:
            num = num * self._base + self._letters.index(char)

        return num
    
    
if __name__ == "__main__":
    try:
        conv = Converter()
        i = 0
        while i < 10:
            x = randint(1, 9999)
            short = conv.convertToURL(x)
            num = conv.convertToNum(short)
            assert num == x
            i += 1

        conv = Converter()
        assert 'bb' == conv.convertToURL(63)
        assert 'ba' == conv.convertToURL(62)
        assert '8' == conv.convertToURL(61)
        print "Test successful!"
        
    except:
        print "Test Failed!"