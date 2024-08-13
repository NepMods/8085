from .ram import RAM8085
class Register8085:
    def __init__(self, bit_width = 8, name = "reg", p = False):
        self.name = name
        self.p = p
        if bit_width not in (8, 16):
            raise ValueError("Bit width must be 8 or 16")
        self.bit_width = bit_width
        if bit_width == 8:
            self.value = 0
        elif bit_width == 16:
            self.value = 0

    def read(self):
        print(self.name, "-> ", self.value) if self.p == True else None
        return self.value

    def set(self, value):

        print(self.name, "<- ", value) if self.p == True else None
        self.value = value

    def get(self):

        print(self.name, "-> ", self.value) if self.p == True else None
        return self.value

    def split_hex_address(self, address):
        lower_byte = address & 0xFF
        higher_byte = (address >> 8) & 0xFF
        lower_byte_hex = lower_byte
        higher_byte_hex = higher_byte

        return lower_byte_hex, higher_byte_hex

    def write(self, value):

        print(self.name, "<-", value) if self.p == True else None
        if self.bit_width == 8:
            if not (0 <= value <= 0xFF):
                raise ValueError("Value must be a byte (0x00 to 0xFF) for 8-bit register")
            self.value = value
        elif self.bit_width == 16:
            if not (0 <= value <= 0xFFFF):
                raise ValueError("Value must be a word (0x0000 to 0xFFFF) for 16-bit register")
            self.value = value

    def __repr__(self):
        return f"Register8085(bit_width={self.bit_width}, value={hex(self.value)})"

class RegisterPair8085(Register8085):
    def __init__(self, reg1 : Register8085, reg2: Register8085, ram : RAM8085, name = "PAIR", p = False):
        self.name =name
        self.p = p
        self.reg1 : Register8085 = reg1
        self.reg2 : Register8085 = reg2
        self.ram : RAM8085 = ram

        if(self.reg1.bit_width != 8 and self.reg2.bit_width != 8):
            raise ValueError("Both register must be 8bits")

    def read(self):
        str_value = f"{self.reg1.read():02X}{self.reg2.read():02X}"
        print(self.name, "-> ", str_value) if self.p == True else None
        address =  int(str_value, 16)
        return self.ram.read(address)

    def set(self, value):
        lower_value, higher_value= self.split_hex_address(value)
        self.reg1.write(higher_value)
        self.reg2.write(lower_value)
        print(self.name, "<- ", value) if self.p == True else None


    def get(self):
        str_value = f"{self.reg1.read():02X}{self.reg2.read():02X}"
        address =  int(str_value, 16)

        print(self.name, "-> ", str_value) if self.p == True else None
        return address

    def write(self, value):
        lower_value, higher_value= self.split_hex_address(value)
        str_value = f"{self.reg1.read():02X}{self.reg2.read():02X}"
        address = int(str_value, 16)

        print(self.name, "<-", str_value) if self.p == True else None
        self.ram.write(address, lower_value)

    def write_16(self, value):
        lower_value, higher_value= self.split_hex_address(value)
        str_value = f"{self.reg1.read():02X}{self.reg2.read():02X}"
        address = int(str_value, 16)
        self.ram.write(address, lower_value)

        print(self.name, "<-", str_value) if self.p == True else None
        self.ram.write(address+1, higher_value)

    def split_hex_address(self, address):
        lower_byte = address & 0xFF
        higher_byte = (address >> 8) & 0xFF
        lower_byte_hex = lower_byte
        higher_byte_hex = higher_byte

        return lower_byte_hex, higher_byte_hex
