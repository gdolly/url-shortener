import unittest

from sample import Sample


class SampleTest(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(Sample().x, 1)


if __name__ == '__main__':
    unittest.main()
