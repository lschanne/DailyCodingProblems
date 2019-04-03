'''
March 1, 2019

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:
- record(order_id): adds the order_id to the log
- get_last(i): gets the ith last element from the log. i is guaranteed to be
  smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

class WebApi:
    def __init__(self, N=None):
        self.N = self._validate_N(N)
        self.stack = [None for _ in range(self.N)]

    def _validate_N(self, N):
        get_N = False
        try:
            N = int(N)
        except (TypeError, ValueError):
            N = None

        if not isinstance(N, int) or N <= 0:
            print('The given N is not a positive integer.')
            print('You will be prompted to enter a new value for N.')
            get_N = True

        while get_N:
            try:
                N = int(raw_input(
                    'Enter a value for N (the number of ids to record): '
                ))
            except (TypeError, ValueError):
                print('"{}" is not a valid integer!'.format(N))
                continue

            if N <= 0:
                print('N must be a positive integer!')
            else:
                get_N = False

        return N

    def record(self, order_id):
        for i in range(self.N - 1):
            self.stack[i] = self.stack[i + 1]

        self.stack[-1] = order_id

    def get_last(self, i):
        idx = self.N - 1 - i
        if not 0 <= idx < N:
            raise ValueError(
                'i ({:.0f}) must be < N ({:.0f}) and >= 0'.format(i, self.N)
            )

        return self.stack[idx]

    def get_command(self):
        '''
        Use command prompts to interface with the API. Only return a non-None
        if the user wants to quit.
        '''

        help_text = (
            '''
            You are interfacing with our Web API. We store up to {:.0f}
            order id's. Use the `record <id>` command to record a new id.
            Use the `get_last <i>` command to get the ith last order id.
            Enter `q` to quit.
            '''
        ).format(self.N)

        while True:
            inpt = raw_input('Enter a command (type `help` for help): ').split()
            command = inpt[0]
            if command == 'q':
                print('Goodbye.')
                return True

            if command == 'help':
                print(help_text)
                return False

            if command not in ['record', 'get_last']:
                print('`{}` is not a valid command!'.format(command))
                continue

            if len(inpt) < 2:
                print(
                    'The `{}` command requires two raw_inputs!'.format(command)
                )
                continue

            try:
                i = int(inpt[1])
            except ValueError:
                print(
                    'The second raw_input of `{}` must be an int!'.format(
                        command
                    )
                )
                continue

            if command == 'record':
                self.record(i)
                print(
                    '{:.0f} has been recorded as the latest order id.'.format(
                        i
                    )
                )
                return False

            if command == 'get_last':
                try:
                    order_id = self.get_last(i)
                except ValueError as e:
                    print('The given index is no good: {}'.format(e))
                    continue

                print('The {:.0f} last order id is: {}'.format(i, order_id))
                return False

if __name__ == '__main__':
    import sys
    N = sys.argv[1] if len(sys.argv) > 1 else None
    api = WebApi(N)
    while True:
        result = api.get_command()
        if result:
            break
