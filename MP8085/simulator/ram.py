class RAM8085:
    def __init__(self):
        self.size = 64 * 1024
        self.memory = bytearray(self.size)

    def read(self, address):
        if not (0 <= address < self.size):
            raise IndexError("Address out of range")
        return self.memory[address]

    def write(self, address, value):
        if not (0 <= address < self.size):
            raise IndexError("Address out of range")
        if not (0 <= value <= 0xFF):
            raise ValueError("Value must be a byte (0x00 to 0xFF)")
        self.memory[address] = value

    def dump(self, start, end):
        if not (0 <= start <= end < self.size):
            raise IndexError("Address out of range")
        return self.memory[start:end+1]

    def dump_to_file(self, filename):
        with open(filename, 'wb') as file:
            file.write(self.memory)

    def __repr__(self):
        return f"RAM8085(size={self.size})"

# Example usage

