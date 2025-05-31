class SharedMemory:
    def __init__(self):
        self.data = []

    def store(self, **kwargs):
        self.data.append(kwargs)

    def get_all(self):
        return self.data
