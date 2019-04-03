'''
February 24, 2019

Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a
prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.
'''

class AutoComplete:
    def __init__(self, string_set):
        self._preprocess(string_set)

    def _preprocess(self, string_set):
        self.lookup_table = {'': set()}
        for s in string_set:
            self.add_string(s)

    def add_string(self, string):
        s = ''
        self.lookup_table[s].add(string)

        for c in string:
            s += c
            self.lookup_table[s] = self.lookup_table.get(s, set()) | {string}

    def query(self, string):
        return self.lookup_table.get(string, set())

if __name__ == '__main__':
    import sys
    if sys.version_info.major > 2:
        raw_input = input

    autocompleter = AutoComplete(sys.argv[1:])
    while 1:
        s = raw_input('Enter a string to autocomplete (Enter "!q" to exit.): ')
        if s == '!q':
            print('Exiting the program...')
            sys.exit()

        print(autocompleter.query(s))