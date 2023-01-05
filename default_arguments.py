class Stream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream):
    for _ in range(n):
        print(stream.get_next())

queries = int(input())
defaults = {"even": 0, "odd": 1}

for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    stream = Stream()
    stream.current = defaults[stream_name]
    print_from_stream(n, stream)
