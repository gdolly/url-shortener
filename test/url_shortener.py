import unittest

from urlshortener import UrlShortener, MaxUrlLimitReachedException, InvalidUrlPassedException, LongUrlNotFoundException


class UrlShortenerTest(unittest.TestCase):
    def test_url_shortener(self):
        url_shortener = UrlShortener()
        self.assertEqual(url_shortener.get_short_url("https://www.revolut.com/rewards-personalised-cashback-and-discounts/"),
                         "https://www.rev.me/1")
        self.assertEqual(url_shortener.get_short_url("https://www.revolut.com/other-url/"), "https://www.rev.me/2")

    def test_url_shortener_should_generate_unique_short_urls_for_same_long_url(self):
        url_shortener = UrlShortener()
        self.assertEqual(url_shortener.get_short_url("https://www.revolut.com/rewards-personalised-cashback-and-discounts/"),
                         "https://www.rev.me/1")
        self.assertEqual(url_shortener.get_short_url("https://www.revolut.com/rewards-personalised-cashback-and-discounts/"), "https://www.rev.me/2")

    def test_url_shortener_should_generate_unique_short_urls_for_same_long_url(self):
        url_shortener = UrlShortener()
        with self.assertRaises(InvalidUrlPassedException):
            url_shortener.get_short_url("")

    def test_url_shortener_for_url_limit(self):
        url_shortener = UrlShortener()
        for i in range(99):
            url_shortener.get_short_url("https://www.revolut.com/other-url/")
        with self.assertRaises(MaxUrlLimitReachedException):
            url_shortener.get_short_url("https://www.revolut.com/other-url/")


    def test_get_long_url_from_short_url(self):
        url_shortener = UrlShortener()
        long_url = "https://www.revolut.com/rewards-personalised-cashback-and-discounts/"
        short_url = url_shortener.get_short_url(long_url)
        self.assertEqual(url_shortener.get_long_url(short_url), long_url)

    def test_get_long_url_fails_with_not_found(self):
        url_shortener = UrlShortener()
        short_url = "https://www.revolut.com/not-found"
        with self.assertRaises(LongUrlNotFoundException):
            url_shortener.get_long_url(short_url)
                         
if __name__ == '__main__':
    unittest.main()
