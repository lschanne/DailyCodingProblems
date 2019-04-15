'''
April 9, 2019

Implement a URL shortener with the following methods:
    shorten(url): shortens the url into a six-character alphanumeric string,
                  such as zLg6wl.
    restore(short): which expands the shortened string into the original url.
                    If no such shortened string exists, return null.

Hint: What if we enter the same URL twice?
'''

import numpy as np

class URLShortener:
    _SHORT_CHARS = (
        [chr(x) for x in range(ord('a'), ord('z') + 1)] +
        [chr(x) for x in range(ord('A'), ord('Z') + 1)] +
        [chr(x) for x in range(ord('0'), ord('9') + 1)]
    )

    def __init__(self, length=6):
        self.length = length
        self._short_dict = {}
        self._long_dict = {}

    def _generate_short(self):
        # This method will have some major performance issues once you start
        # to fill up a lot of the available permutations
        # One alternative would be to generate all possible permutations
        # in the __init__ and then iterate over them here
        # I guess which method you use depends on your needs (estimated number
        # of urls that will be shortened)
        while True:
            short = ''.join(
                np.random.choice(self._SHORT_CHARS, size=self.length)
            )
            if not short in self._short_dict:
                return short

    def shorten(self, url):
        short = self._long_dict.get(url)
        if not short:
            short = self._generate_short()
            self._long_dict[url] = short
            self._short_dict[short] = url

        return short

    def restore(self, short):
        return self._short_dict.get(short)

if __name__ == '__main__':
    url_shortener = URLShortener()
    for method, value in zip(
        ('shorten', 'restore', 'shorten', 'shorten', 'restore'),
        (
            'some_url', 'some_url', 'https://www.website.com', 'another url',
            'https://www.website.com',
        ),
    ):
        if method == 'shorten':
            result = url_shortener.shorten(value)
        elif method == 'restore':
            value = url_shortener._long_dict.get(value)
            result = url_shortener.restore(value)
        print(method, value, result)
        print('----------------------')
