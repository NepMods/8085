from .ram import RAM8085
from .registers import Register8085, RegisterPair8085
from .ALU import ALU8085
from .IO import IO8085
from .FlipFlop import FF8085
class CPU8085:
    def __init__(self):
        self.ram = RAM8085()

        self.A = Register8085(bit_width=8, name = "A", p=True)
        self.PSW = Register8085(bit_width=8, name = "psw")

        self.B = Register8085(bit_width=8, name = "B")
        self.C = Register8085(bit_width=8, name = "C")
        self.D = Register8085(bit_width=8, name = "D")
        self.E = Register8085(bit_width=8, name = "E")
        self.H = Register8085(bit_width=8, name = "H")
        self.L = Register8085(bit_width=8, name = "L")

        self.BC = RegisterPair8085(self.B, self.C, self.ram, name = "BC")
        self.DE = RegisterPair8085(self.D, self.E, self.ram, name="DE")
        self.HL = RegisterPair8085(self.H, self.L, self.ram, name="HL")
        self.M = RegisterPair8085(self.H, self.L, self.ram, name="M")

        self.PC = Register8085(bit_width=16, name = "PC")
        self.SP = Register8085(bit_width=16, name = "SP")
        self.IR = Register8085(bit_width=16, name = "IR")

        self.FLAGS = Register8085(bit_width=8, name = "FLAGS")
        self.alu = ALU8085(self.FLAGS)

        self.IO0 = IO8085()
        self.IO1 = IO8085()
        self.IO2 = IO8085()
        self.IO3 = IO8085()
        self.IO4 = IO8085()
        self.IO5 = IO8085()
        self.IO6 = IO8085()
        self.IO7 = IO8085()

        self.IE = FF8085()
        self.IM7_5 = FF8085()
        self.IM6_5 = FF8085()
        self.IM5_5 = FF8085()


        self.operations = {'A8': {'opcode': 'XRA', }, 'A9': {'opcode': 'XRA', },
                    'AA': {'opcode': 'XRA', }, 'AB': {'opcode': 'XRA', },
                    'AC': {'opcode': 'XRA', }, 'AD': {'opcode': 'XRA', },
                    'AE': {'opcode': 'XRA', }, 'AF': {'opcode': 'XRA', },
                    'A0': {'opcode': 'ANA', }, 'A1': {'opcode': 'ANA', },
                    'A2': {'opcode': 'ANA', }, 'A3': {'opcode': 'ANA', },
                    'A4': {'opcode': 'ANA', }, 'A5': {'opcode': 'ANA', },
                    'A6': {'opcode': 'ANA', }, 'A7': {'opcode': 'ANA', },
                    '80': {'opcode': 'ADD', }, '81': {'opcode': 'ADD', },
                    '82': {'opcode': 'ADD', }, '83': {'opcode': 'ADD', },
                    '84': {'opcode': 'ADD', }, '85': {'opcode': 'ADD', },
                    '86': {'opcode': 'ADD', }, '87': {'opcode': 'ADD', },
                    '88': {'opcode': 'ADC', }, '89': {'opcode': 'ADC', },
                    '8A': {'opcode': 'ADC', }, '8B': {'opcode': 'ADC', },
                    '8C': {'opcode': 'ADC', }, '8D': {'opcode': 'ADC', },
                    '8E': {'opcode': 'ADC', }, '8F': {'opcode': 'ADC', },
                    '0B': {'opcode': 'DCX', }, '1B': {'opcode': 'DCX', },
                    '2B': {'opcode': 'DCX', }, '3B': {'opcode': 'DCX', },
                    '05': {'opcode': 'DCR', }, '0D': {'opcode': 'DCR', },
                    '15': {'opcode': 'DCR', }, '1D': {'opcode': 'DCR', },
                    '25': {'opcode': 'DCR', }, '2D': {'opcode': 'DCR', },
                    '35': {'opcode': 'DCR', }, '3D': {'opcode': 'DCR', },
                    '06': {'opcode': 'MVI', }, '0E': {'opcode': 'MVI', },
                    '16': {'opcode': 'MVI', }, '1E': {'opcode': 'MVI', },
                    '26': {'opcode': 'MVI', }, '2E': {'opcode': 'MVI', },
                    '36': {'opcode': 'MVI', }, '3E': {'opcode': 'MVI', },
                    'B0': {'opcode': 'ORA', }, 'B1': {'opcode': 'ORA', },
                    'B2': {'opcode': 'ORA', }, 'B3': {'opcode': 'ORA', },
                    'B4': {'opcode': 'ORA', }, 'B5': {'opcode': 'ORA', },
                    'B6': {'opcode': 'ORA', }, 'B7': {'opcode': 'ORA', },
                    '90': {'opcode': 'SUB', }, '91': {'opcode': 'SUB', },
                    '92': {'opcode': 'SUB', }, '93': {'opcode': 'SUB', },
                    '94': {'opcode': 'SUB', }, '95': {'opcode': 'SUB', },
                    '96': {'opcode': 'SUB', }, '97': {'opcode': 'SUB', },
                    'C7': {'opcode': 'RST', }, 'CF': {'opcode': 'RST', },
                    'D7': {'opcode': 'RST', }, 'DF': {'opcode': 'RST', },
                    'E7': {'opcode': 'RST', }, 'EF': {'opcode': 'RST', },
                    'F7': {'opcode': 'RST', }, 'FF': {'opcode': 'RST', },
                    '98': {'opcode': 'SBB', }, '99': {'opcode': 'SBB', },
                    '9A': {'opcode': 'SBB', }, '9B': {'opcode': 'SBB', },
                    '9C': {'opcode': 'SBB', }, '9D': {'opcode': 'SBB', },
                    '9E': {'opcode': 'SBB', }, '9F': {'opcode': 'SBB', },
                    'C1': {'opcode': 'POP', }, 'D1': {'opcode': 'POP', },
                    'E1': {'opcode': 'POP', }, 'F1': {'opcode': 'POP', },
                    'C5': {'opcode': 'PUSH', }, 'D5': {'opcode': 'PUSH', },
                    'E5': {'opcode': 'PUSH', }, 'F5': {'opcode': 'PUSH', },
                    '01': {'opcode': 'LXI', }, '11': {'opcode': 'LXI', },
                    '21': {'opcode': 'LXI', }, '31': {'opcode': 'LXI', },
                    '04': {'opcode': 'INR', }, '0C': {'opcode': 'INR', },
                    '14': {'opcode': 'INR', }, '1C': {'opcode': 'INR', },
                    '24': {'opcode': 'INR', }, '2C': {'opcode': 'INR', },
                    '34': {'opcode': 'INR', }, '3C': {'opcode': 'INR', },
                    '03': {'opcode': 'INX', }, '13': {'opcode': 'INX', },
                    '23': {'opcode': 'INX', }, '33': {'opcode': 'INX', },
                    '0A': {'opcode': 'LDAX', }, '1A': {'opcode': 'LDAX', },
                    'B8': {'opcode': 'CMP', }, 'B9': {'opcode': 'CMP', },
                    'BA': {'opcode': 'CMP', }, 'BB': {'opcode': 'CMP', },
                    'BC': {'opcode': 'CMP', }, 'BD': {'opcode': 'CMP', },
                    'BE': {'opcode': 'CMP', }, 'BF': {'opcode': 'CMP', },
                    '09': {'opcode': 'DAD', }, '19': {'opcode': 'DAD', },
                    '29': {'opcode': 'DAD', }, '39': {'opcode': 'DAD', },
                    '40': {'opcode': 'MOV', },
                    '41': {'opcode': 'MOV', },
                    '42': {'opcode': 'MOV', },
                    '43': {'opcode': 'MOV', },
                    '44': {'opcode': 'MOV', },
                    '45': {'opcode': 'MOV', },
                    '46': {'opcode': 'MOV', },
                    '47': {'opcode': 'MOV', },
                    '48': {'opcode': 'MOV', },
                    '49': {'opcode': 'MOV', },
                    '4A': {'opcode': 'MOV', },
                    '4B': {'opcode': 'MOV', },
                    '4C': {'opcode': 'MOV', },
                    '4D': {'opcode': 'MOV', },
                    '4E': {'opcode': 'MOV', },
                    '4F': {'opcode': 'MOV', },
                    '50': {'opcode': 'MOV', },
                    '51': {'opcode': 'MOV', },
                    '52': {'opcode': 'MOV', },
                    '53': {'opcode': 'MOV', },
                    '54': {'opcode': 'MOV', },
                    '55': {'opcode': 'MOV', },
                    '56': {'opcode': 'MOV', },
                    '57': {'opcode': 'MOV', },
                    '58': {'opcode': 'MOV', },
                    '59': {'opcode': 'MOV', },
                    '5A': {'opcode': 'MOV', },
                    '5B': {'opcode': 'MOV', },
                    '5C': {'opcode': 'MOV', },
                    '5D': {'opcode': 'MOV', },
                    '5E': {'opcode': 'MOV', },
                    '5F': {'opcode': 'MOV', },
                    '60': {'opcode': 'MOV', },
                    '61': {'opcode': 'MOV', },
                    '62': {'opcode': 'MOV', },
                    '63': {'opcode': 'MOV', },
                    '64': {'opcode': 'MOV', },
                    '65': {'opcode': 'MOV', },
                    '66': {'opcode': 'MOV', },
                    '67': {'opcode': 'MOV', },
                    '68': {'opcode': 'MOV', },
                    '69': {'opcode': 'MOV', },
                    '6A': {'opcode': 'MOV', },
                    '6B': {'opcode': 'MOV', },
                    '6C': {'opcode': 'MOV', },
                    '6D': {'opcode': 'MOV', },
                    '6E': {'opcode': 'MOV', },
                    '6F': {'opcode': 'MOV', },
                    '70': {'opcode': 'MOV', },
                    '71': {'opcode': 'MOV', },
                    '72': {'opcode': 'MOV', },
                    '73': {'opcode': 'MOV', },
                    '74': {'opcode': 'MOV', },
                    '75': {'opcode': 'MOV', },
                    '77': {'opcode': 'MOV', },
                    '78': {'opcode': 'MOV', },
                    '79': {'opcode': 'MOV', },
                    '7A': {'opcode': 'MOV', },
                    '7B': {'opcode': 'MOV', },
                    '7C': {'opcode': 'MOV', },
                    '7D': {'opcode': 'MOV', },
                    '7E': {'opcode': 'MOV', },
                    '7F': {'opcode': 'MOV', }, 'CE': {'opcode': 'ACI', },
                    'C6': {'opcode': 'ADI', }, 'E6': {'opcode': 'ANI', },
                    'CD': {'opcode': 'CALL', }, '2F': {'opcode': 'CMA', },
                    '3F': {'opcode': 'CMC', }, 'FE': {'opcode': 'CPI', },
                    '27': {'opcode': 'DAA', }, 'F3': {'opcode': 'DI', },
                    'FB': {'opcode': 'EI', }, '76': {'opcode': 'HLT', },
                    'DB': {'opcode': 'IN', }, 'C3': {'opcode': 'JMP', },
                    'DA': {'opcode': 'JC', }, 'D2': {'opcode': 'JNC', },
                    'F2': {'opcode': 'JP', }, 'FA': {'opcode': 'JM', },
                    'EA': {'opcode': 'JPE', }, 'E2': {'opcode': 'JPO', },
                    'CA': {'opcode': 'JZ', }, 'C2': {'opcode': 'JNZ', },
                    '3A': {'opcode': 'LDA', }, '2A': {'opcode': 'LHLD', },
                    '00': {'opcode': 'NOP', }, 'F6': {'opcode': 'ORI', },
                    'D3': {'opcode': 'OUT', }, 'E9': {'opcode': 'PCHL', },
                    '17': {'opcode': 'RAL', }, '1F': {'opcode': 'RAR', },
                    '07': {'opcode': 'RLC', }, '0F': {'opcode': 'RRC', },
                    'C9': {'opcode': 'RET', }, 'D8': {'opcode': 'RC', },
                    'D0': {'opcode': 'RNC', }, 'F0': {'opcode': 'RP', },
                    'F8': {'opcode': 'RM', }, 'E8': {'opcode': 'RPE', },
                    'E0': {'opcode': 'RPO', }, 'C8': {'opcode': 'RZ', },
                    'C0': {'opcode': 'RNZ', }, '20': {'opcode': 'RIM', },
                    'DE': {'opcode': 'SBI', }, '22': {'opcode': 'SHLD', },
                    '30': {'opcode': 'SIM', }, 'F9': {'opcode': 'SPHL', },
                    '32': {'opcode': 'STA', }, '37': {'opcode': 'STC', },
                    'D6': {'opcode': 'SUI', }, 'EB': {'opcode': 'XCHG', },
                    'E3': {'opcode': 'XTHL', }, 'EE': {'opcode': 'XRI', },
                    '02': {'opcode': 'STAX', }, '12': {'opcode': 'STAX', }}

    def getSize(self, op) -> int:
        sizes = {
            "MOV": 1, "MVI": 2, "LDAX": 1, "LHLD": 3, "LDA": 3, "STAX": 1, "SHLD": 3, "STA": 3,
            "LXI": 3, "SPHL": 1, "XTHL": 1, "XCHG": 1, "OUT": 2, "IN": 2, "PUSH": 1, "POP": 1,
            "ADD": 1, "ADC": 1, "ADI": 2, "ACI": 2, "SUB": 1, "SBB": 1, "SUI": 2, "SBI": 2,
            "DAD": 1, "DAA": 1, "INR": 1, "INX": 1, "DCR": 1, "DCX": 1, "STC": 1, "ANA": 1,
            "ANI": 2, "XRA": 1, "XRI": 2, "ORA": 1, "ORI": 2, "CMP": 1, "CPI": 2, "RLC": 1,
            "RRC": 1, "RAL": 1, "RAR": 1, "CMA": 1, "CMC": 1, "JMP": 3, "JC": 3, "JNC": 3,
            "JP": 3, "JM": 3, "JPE": 3, "JPO": 3, "JZ": 3, "JNZ": 3, "PCHL": 1, "RST": 1,
            "CALL": 3, "CC": 3, "CNC": 3, "CP": 3, "CM": 3, "CPE": 3, "CPO": 3, "CZ": 3,
            "CNZ": 3, "RET": 1, "RC": 1, "RNC": 1, "RP": 1, "RM": 1, "RPE": 1, "RPO": 1,
            "RZ": 1, "RNZ": 1, "NOP": 1, "HLT": 1, "DI": 1, "EI": 1, "RIM": 1, "SIM": 1
        }
        return sizes.get(op.upper(), "Invalid instruction")

    def decode_flag(self, flag):
        flags = bin(flag)[2:].zfill(8)
        S = flags[0]
        Z = flags[1]
        AC = flags[3]
        P = flags[5]
        C = flags[7]
        return S, Z, AC, P, C

    def replace_flag(self, at, value):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if at == 0:
            S = value
        elif at == 1:
            Z = value
        elif at == 2:
            AC = value
        elif at == 3:
            P = value
        elif at == 4:
            C = value

        flag = self.alu.encode_flag(S, Z, AC, P, C)
        self.FLAGS.write(flag)

    def get_carry(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        return int(C)

    def set_carry(self, value):
        self.replace_flag(4, value)

    def MOV(self, register1 : Register8085, register2 : Register8085):
        register1.write(register2.read())

    def MVI(self, register : Register8085, value):
        register.write(value)

    def LDAX(self, regp : RegisterPair8085):
        self.A.write(regp.read())

    def LHLD(self, address):
        lower = self.ram.read(address)
        higher = self.ram.read(address+1)
        self.H.write(higher)
        self.L.write(lower)

    def LDA(self, address):
        value = self.ram.read(address)
        self.A.write(value)

    def STAX(self, reg : RegisterPair8085):
        reg.write(self.A.read())

    def SHLD(self, address):
        self.ram.write(address, self.L.read())
        self.ram.write(address+1, self.H.read())

    def STA(self, address):
        self.ram.write(address, self.A.read())

    def LXI(self, reg : RegisterPair8085, value):
        reg.set(value)

    def SPHL(self):
        self.SP.set(self.HL.get())

    def XTHL(self):
        hl = self.HL.get()
        sp = self.SP.get()
        lower, higher = self.HL.split_hex_address(hl)
        lower_m = self.ram.read(sp)
        higher_m = self.ram.read(sp+1)
        self.ram.write(sp, lower)
        self.ram.write(sp+1, higher)
        self.H.write(higher_m)
        self.L.write(lower_m)

    def XCHG(self):
        hl = self.HL.get()
        de = self.DE.get()
        self.HL.set(de)
        self.DE.set(hl)

    def OUT(self, port : IO8085):
        port.write(self.A.read())

    def IN(self, port : IO8085):
        self.A.write(port.read())

    def PUSH(self, pair : RegisterPair8085):
        sp_address = self.SP.get()
        lower, higher = pair.split_hex_address(pair.get())
        store_addr = sp_address - 2
        self.ram.write(store_addr, lower)
        self.ram.write(store_addr+1, higher)
        self.SP.set(store_addr)

    def POP(self, pair : RegisterPair8085):
        sp_address = self.SP.get()
        store_addr = sp_address + 2

        lower = self.ram.read(sp_address)
        higher = self.ram.read(sp_address+1)

        str_value = f"{higher:02X}{lower:02X}"
        address =  int(str_value, 16)
        self.SP.set(store_addr)
        pair.set(address)

    def ADD(self, register: Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result = self.alu.add(reg_value, acc_value) & 0xFF
        self.A.write(result)

    def ADC(self, register: Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result_before = self.alu.add(reg_value, self.get_carry())
        result = self.alu.add(result_before, acc_value)
        self.A.write(result)

    def ADI(self, value):
        acc_value = self.A.read()
        result = self.alu.add(value, acc_value)
        self.A.write(result)

    def ACI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result_before = self.alu.add(acc_value, self.get_carry())
        result = self.alu.add(reg_value, result_before)
        self.A.write(result)

    def SUB(self, register: Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result = self.alu.subtract(acc_value, reg_value)
        self.A.write(result)

    def SBB(self, register: Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result_before = self.alu.add(reg_value, self.get_carry())
        result = self.alu.subtract(acc_value, result_before)
        self.A.write(result)

    def SUI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result = self.alu.subtract(acc_value, reg_value)
        self.A.write(result)

    def SBI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result_prev = self.alu.subtract(acc_value, self.get_carry())
        result = self.alu.subtract(result_prev, reg_value)
        self.A.write(result)

    def DAD(self, pair : RegisterPair8085):
        reg_value = pair.get()
        HL_value = self.HL.get()

        value = self.alu.add(reg_value, HL_value, True)
        if(value > 0xFFFF):
            self.replace_flag(4, 1)

        real_value = value & 0xFFFF
        self.HL.set(real_value)

    def DAA(self):
        acc_value = self.A.read()
        self.A.write(int(f"{acc_value}", 16))


    def INR(self, register : Register8085):
        reg_value = register.read()
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        acc_value = self.alu.add(reg_value, 0x1)
        self.replace_flag(4, C)
        register.write(acc_value)

    def INX(self, registerPair : RegisterPair8085):
        reg_value = registerPair.get()
        registerPair.set(reg_value+1)

    def DCR(self, register : Register8085):
        reg_value = register.read()
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        acc_value = self.alu.subtract(reg_value, 0x1)
        self.replace_flag(4, C)
        register.write(acc_value)

    def DCX(self, register : RegisterPair8085):
        reg_value = register.get()
        acc_value = self.alu.subtract_16(reg_value, 0x1, True)
        register.set(acc_value)

    def DI(self):
        self.IE.reset()

    def EI(self):
        self.IE.set()

    def STC(self):
        self.replace_flag(4, 1)

    def ANA(self, register : Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result = self.alu.and_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def ANI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result = self.alu.and_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def XRA(self, register : Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result = self.alu.xor_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def XRI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result = self.alu.xor_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def ORA(self, register : Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        result = self.alu.or_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def ORI(self, value):
        reg_value = value
        acc_value = self.A.read()
        result = self.alu.or_op(reg_value, acc_value)
        self.replace_flag(4, 0)
        self.replace_flag(2, 1)
        self.A.write(result)

    def CMP(self, register : Register8085):
        reg_value = register.read()
        acc_value = self.A.read()
        self.alu.subtract(acc_value, reg_value)

    def CPI(self, value):
        reg_value = value
        acc_value = self.A.read()
        self.alu.subtract(acc_value, reg_value)

    def RLC(self):
        acc_value = self.A.read()
        result = self.alu.rotate_left(acc_value)
        self.A.write(result)

    def RRC(self):
        acc_value = self.A.read()
        result = self.alu.rotate_right(acc_value)
        self.A.write(result)

    def RAL(self):
        acc_value = self.A.read()
        result = self.alu.ral(acc_value)
        self.A.write(result)

    def RAR(self):
        acc_value = self.A.read()
        result = self.alu.rar(acc_value)
        self.A.write(result)

    def CMA(self):
        acc_value = self.A.read()
        comp = int("FF", 16) - acc_value
        self.A.write(comp)

    def CMC(self):
        acc_value = self.get_carry()
        comp = 1 - acc_value
        self.set_carry(comp)

    def JMP(self, address):
        self.PC.write(address)

    def JC(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 1):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def JNC(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 0):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def JP(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 0):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def JM(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 1):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def PCHL(self):
        hl_val = self.HL.get()
        self.PC.set(hl_val)

    def RST(self, value):
        if value == 0:
            self.PC.set(int("0000", 16))
        if value == 1:
            self.PC.set(int("0008", 16))
        if value == 2:
            self.PC.set(int("0010", 16))
        if value == 3:
            self.PC.set(int("0018", 16))
        if value == 4:
            self.PC.set(int("0020", 16))
        if value == 5:
            self.PC.set(int("0028", 16))
        if value == 6:
            self.PC.set(int("0030", 16))
        if value == 7:
            self.PC.set(int("0038", 16))

    def JPO(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 0):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def JPE(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 1):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)


    def JZ(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 1):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def JNZ(self, address):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 0):
            self.PC.write(address)
        else:
            self.PC.write(self.PC.read()+3)

    def CALL(self, address):
        self.PC.write(self.PC.read() + 3)
        self.PUSH(self.PC)
        self.PC.write(address)

    def CC(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 1):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CNC(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 0):
            self.PUSH(self.PC)
            self.PC.write(address)

    def CP(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 0):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CM(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 1):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CPO(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 0):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CPE(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 1):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CZ(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 1):
            self.PUSH(self.PC)
            self.PC.write(address)


    def CNZ(self, address):
        self.PC.write(self.PC.read() + 3)
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 0):
            self.PUSH(self.PC)
            self.PC.write(address)

    def RET(self):
        self.POP(self.PC)

    def RC(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 1):
            self.POP(self.PC)

    def RNC(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(C) == 0):
            self.POP(self.PC)

    def RP(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 0):
            self.POP(self.PC)

    def RM(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(S) == 1):
            self.POP(self.PC)

    def RPO(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 0):
            self.POP(self.PC)

    def RPE(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(P) == 1):
            self.POP(self.PC)

    def RZ(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 1):
            self.POP(self.PC)

    def RNZ(self):
        S, Z, AC, P, C = self.decode_flag(self.FLAGS.read())
        if (int(Z) == 0):
            self.POP(self.PC)

    def NOP(self):
        return

    def HLT(self):
        return

    def RIM(self):
        return

    def SIM(self):
        return