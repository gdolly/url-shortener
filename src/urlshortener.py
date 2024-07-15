class UrlShortener:
    MAX_URLS_SUPPORTED = 100
    def __init__(self):
        self.counter= 1
        self.database = {}
    def get_short_url(self, long_url):
        if long_url == "":
            raise InvalidUrlPassedException
        short_url = f"https://www.rev.me/{self.counter}"
        self.counter += 1
        if self.counter > self.MAX_URLS_SUPPORTED:
            raise MaxUrlLimitReachedException
        self.database[short_url] = long_url
        return short_url

    def get_long_url(self, short_url):
        if short_url in self.database:
            return self.database[short_url]
        else: raise LongUrlNotFoundException


class MaxUrlLimitReachedException(Exception):
    pass

class InvalidUrlPassedException(Exception):
    pass


class LongUrlNotFoundException(Exception):
    pass

