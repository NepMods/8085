
class IO8085:
    def __init__(self):
        self.bit_width = 8
        self.value = 0

    def read(self):
        return self.value

    def set(self, value):
        self.value = value

    def get(self):
        return self.value

    def write(self, value):
        if self.bit_width == 8:
            if not (0 <= value <= 0xFF):
                raise ValueError("Value must be a byte (0x00 to 0xFF) for I/O port")
            self.value = value

