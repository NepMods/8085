def validate_8(value):
    if not (0 <= value <= 0xFF):
        raise ValueError("Value must be a byte (0x00 to 0xFF) for 8-bit")

def validate_16(value):
    if not (0 <= value <= 0xFFFF):
        raise ValueError("Value must be a word (0x0000 to 0xFFFF) for 16-bit")

def ACI(value: int) -> str:
    validate_8(value)
    return f"CE {value:02X}".upper()

def ADC(source: str) -> str:
    table = {"B": "88", "C": "89", "D": "8A", "E": "8B", "H": "8C", "L": "8D", "M": "8E", "A": "8F"}
    return table.get(source.upper(), "Invalid Register or Pair")

def ADD(source: str) -> str:
    table = {"B": "80", "C": "81", "D": "82", "E": "83", "H": "84", "L": "85", "M": "86", "A": "87"}
    return table.get(source.upper(), "Invalid Register or Pair")

def ADI(value: int) -> str:
    validate_8(value)
    return f"C6 {value:02X}".upper()

def ANA(source: str) -> str:
    table = {"B": "A0", "C": "A1", "D": "A2", "E": "A3", "H": "A4", "L": "A5", "M": "A6", "A": "A7"}
    return table.get(source.upper(), "Invalid Register or Pair")

def ANI(value: int) -> str:
    validate_8(value)
    return f"E6 {value:02X}".upper()

def CALL(address: int) -> str:
    validate_8(16)
    high_byte = (address >> 8) & 0xFF
    low_byte = address & 0xFF
    return f"CD {low_byte:02X} {high_byte:02X}"

def CMA() -> str:
    return "2F"

def CMC() -> str:
    return "3F"

def CMP(source: str) -> str:
    table = {"B": "B8", "C": "B9", "D": "BA", "E": "BB", "H": "BC", "L": "BD", "M": "BE", "A": "BF"}
    return table.get(source.upper(), "Invalid Register or Pair")

def CPI(value: int) -> str:
    validate_8(value)
    return f"FE {value:02X}".upper()

def DAA() -> str:
    return "27"

def DAD(pair: str) -> str:
    table = {"B": "09", "D": "19", "H": "29", "SP": "39"}
    return table.get(pair.upper(), "Invalid Register or Pair")

def DCR(target: str) -> str:
    table = {"B": "05", "C": "0D", "D": "15", "E": "1D", "H": "25", "L": "2D", "M": "35", "A": "3D"}
    return table.get(target.upper(), "Invalid Register or Pair")

def DCX(pair: str) -> str:
    table = {"B": "0B", "D": "1B", "H": "2B", "SP": "3B"}
    return table.get(pair.upper(), "Invalid Register or Pair")

def DI() -> str:
    return "F3"

def EI() -> str:
    return "FB"

def HLT() -> str:
    return "76"

def IN(port: int) -> str:
    if(port > 7 or port < 0):
        raise Exception(f"Unknown Port {port}")
    return f"DB {port:02X}".upper()

def INR(target: str) -> str:
    table = {"B": "04", "C": "0C", "D": "14", "E": "1C", "H": "24", "L": "2C", "M": "34", "A": "3C"}
    return table.get(target.upper(), "Invalid Register or Pair")

def INX(register_pair: str) -> str:
    table = {'B': '03', 'D': '13', 'H': '23', 'SP': '33'}
    return table.get(register_pair.upper(), 'Invalid register pair')

def JMP(address: int) -> str:
    validate_16(address)
    return f"C3 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JC(address: int) -> str:
    validate_16(address)
    return f"DA {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JNC(address: int) -> str:
    validate_16(address)
    return f"D2 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JP(address: int) -> str:
    validate_16(address)
    return f"F2 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JM(address: int) -> str:
    validate_16(address)
    return f"FA {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JPE(address: int) -> str:
    validate_16(address)
    return f"EA {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JPO(address: int) -> str:
    validate_16(address)
    return f"E2 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JZ(address: int) -> str:
    validate_16(address)
    return f"CA {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def JNZ(address: int) -> str:
    validate_16(address)
    return f"C2 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def LDA(address: int) -> str:
    validate_16(address)
    return f"3A {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def LDAX(register_pair: str) -> str:
    table = {'BC': '0A', 'DE': '1A'}
    return table.get(register_pair.upper(), 'Invalid register pair')

def LHLD(address: int) -> str:
    validate_16(address)
    return f"2A {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def LXI(register_pair: str, address: int) -> str:
    validate_16(address)
    table = {'B': '01', 'D': '11', 'H': '21', 'SP': '31'}
    opcode = table.get(register_pair.upper(), 'Invalid register pair')
    if opcode == 'Invalid register pair':
        return opcode
    return f"{opcode} {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}".upper()

def MOV(DEST: str, SOURCE: str) -> str:
    table = {
        'B': ['40', '41', '42', '43', '44', '45', '46', '47'],
        'C': ['48', '49', '4A', '4B', '4C', '4D', '4E', '4F'],
        'D': ['50', '51', '52', '53', '54', '55', '56', '57'],
        'E': ['58', '59', '5A', '5B', '5C', '5D', '5E', '5F'],
        'H': ['60', '61', '62', '63', '64', '65', '66', '67'],
        'L': ['68', '69', '6A', '6B', '6C', '6D', '6E', '6F'],
        'M': ['70', '71', '72', '73', '74', '75', '--', '77'],
        'A': ['78', '79', '7A', '7B', '7C', '7D', '7E', '7F']
    }

    source_index = ['B', 'C', 'D', 'E', 'H', 'L', 'M', 'A'].index(SOURCE.upper())
    destination_index = ['B', 'C', 'D', 'E', 'H', 'L', 'M', 'A'].index(DEST.upper())

    return table.get(DEST.upper(), "Invalid Register or Pair")[source_index]

def MVI(register: str, data: int) -> str:
    validate_8(data)
    table = {'B': '06', 'C': '0E', 'D': '16', 'E': '1E', 'H': '26', 'L': '2E', 'M': '36', 'A': '3E'}
    return f"{table.get(register.upper(), "Invalid Register or Pair")} {data:02X}".upper()

def NOP() -> str:
    return "00"

def ORA(register: str) -> str:
    table = {'B': 'B0', 'C': 'B1', 'D': 'B2', 'E': 'B3', 'H': 'B4', 'L': 'B5', 'M': 'B6', 'A': 'B7'}
    return table.get(register.upper(), 'Invalid register')

def ORI(data: int) -> str:
    validate_8(data)
    return f"F6 {data:02X}".upper()

def OUT(port: int) -> str:

    return f"D3 {port:02X}".upper()

def PCHL() -> str:
    return "E9"

def POP(register_pair: str) -> str:
    table = {'B': 'C1', 'D': 'D1', 'H': 'E1', 'PSW': 'F1'}
    return table.get(register_pair.upper(), 'Invalid register pair')

def PUSH(register_pair: str) -> str:
    table = {'B': 'C5', 'D': 'D5', 'H': 'E5', 'PSW': 'F5'}
    return table.get(register_pair.upper(), 'Invalid register pair')

def RAL() -> str:
    return "17"

def RAR() -> str:
    return "1F"

def RLC() -> str:
    return "07"

def RRC() -> str:
    return "0F"

def RET() -> str:
    return "C9"

def RC() -> str:
    return "D8"

def RNC() -> str:
    return "D0"

def RP() -> str:
    return "F0"

def RM() -> str:
    return "F8"

def RPE() -> str:
    return "E8"

def RPO() -> str:
    return "E0"

def RZ() -> str:
    return "C8"

def RNZ() -> str:
    return "C0"

def RIM() -> str:
    return "20"

def RST(n: int) -> str:
    table = {0: "C7", 1: "CF", 2: "D7", 3: "DF", 4: "E7", 5: "EF", 6: "F7", 7: "FF"}
    return table.get(n, "Invalid RST number")

def SBB(source: str) -> str:
    table = {"B": "98", "C": "99", "D": "9A", "E": "9B", "H": "9C", "L": "9D", "M": "9E", "A": "9F"}
    return table.get(source.upper(), "Invalid source")

def SBI(value: int) -> str:
    validate_8(value)
    return f"DE {value:02X}".upper()

def SHLD(address: int) -> str:
    validate_16(address)
    return f"22 {address:04X}".upper()

def SIM() -> str:
    return "30"

def SPHL() -> str:
    return "F9"

def STA(address: int) -> str:
    validate_16(address)
    if 0 <= address <= 0xFFFF:
        return f"32 {address & 0xFF:02X} {(address >> 8) & 0xFF:02X}"
    else:
        raise ValueError("Address must be between 0x0000 and 0xFFFF")

def STAX(register: str) -> str:
    table = {'B': "02", 'D': "12"}
    return table.get(register.upper(), 'Invalid register')

def STC() -> str:
    return "37"

def SUB(operand: str) -> str:
    table = {'B': "90", 'C': "91", 'D': "92", 'E': "93", 'H': "94", 'L': "95", 'M': "96", 'A': "97"}
    return table.get(operand.upper(), "Invalid Register or Pair")

def SUI(data: int) -> str:
    validate_8(data)
    if 0 <= data <= 0xFF:
        return f"D6 {data:02X}".upper()
    else:
        raise ValueError("Data must be between 0x00 and 0xFF")

def XCHG() -> str:
    return "EB"

def XRA(operand: str) -> str:
    table = {'B': "A8", 'C': "A9", 'D': "AA", 'E': "AB", 'H': "AC", 'L': "AD", 'M': "AE", 'A': "AF"}
    return table.get(operand.upper(), "Invalid Register or Pair")

def XRI(data: int) -> str:
    validate_8(data)
    if 0 <= data <= 0xFF:
        return f"EE {data:02X}".upper()
    else:
        raise ValueError("Data must be between 0x00 and 0xFF")

def XTHL() -> str:
    return "E3"
