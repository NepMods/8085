class FF8085:
    def __init__(self):
        self.value = 0

    def set(self):
        self.value = 1

    def reset(self):
        self.value = 0

    def get(self):
        return self.value