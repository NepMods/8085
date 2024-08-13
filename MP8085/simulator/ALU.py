from .registers import Register8085
class ALU8085:
    def __init__(self, FlagRegister : Register8085):
        self.accumulator = 0
        self.flags : FlagRegister = FlagRegister

    def encode_flag(self, S : int, Z : int, AC : int, P: int, C: int):
        flags = (int(f"{S}{Z}0{AC}0{P}0{C}", 2))
        return flags

    def decode_flag(self, flag):
        flags = bin(flag)[2:].zfill(8)
        S = flags[0]
        Z = flags[1]
        AC = flags[3]
        P = flags[5]
        C = flags[7]
        return S, Z, AC, P, C

    def update_flags(self, result, carry=0, borrow=0):
        S = int(result & 0x80 != 0)
        Z = int(result == 0)
        C = carry
        AC = borrow
        P = int(bin(result).count('1') % 2 == 0)

        flag_value = self.encode_flag(int(S), int(Z), int(AC), int(P), int(C))
        self.flags.write(flag_value)

    def replace_flag(self, at, value):
        S, Z, AC, P, C = self.decode_flag(self.flags.read())
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

        flag = self.encode_flag(S, Z, AC, P, C)
        self.flags.write(flag)

    def add(self, operand1, operand2, NF = False):
        result = (operand1 + operand2) & 0xFF
        carry = (operand1 + operand2) > 0xFF
        auxiliary_carry = ((operand1 & 0x0F) + (operand2 & 0x0F)) > 0x0F
        self.accumulator = result
        if(not NF):
            self.update_flags(result, carry=carry, borrow=auxiliary_carry)
        return result

    def add_16(self, operand1, operand2, NF = False):
        result = (operand1 + operand2) & 0xFFFF
        carry = (operand1 + operand2) > 0xFFFF
        auxiliary_carry = ((operand1 & 0x0F) + (operand2 & 0x0F)) > 0x0F
        self.accumulator = result
        if(not NF):
            self.update_flags(result, carry=carry, borrow=auxiliary_carry)
        return result

    def subtract(self, operand1, operand2, NF = False):
        result = (operand1 - operand2) & 0xFF
        borrow = (operand1 - operand2) < 0
        auxiliary_borrow  = ((operand1 & 0x0F) - (operand2 & 0x0F)) > 0x0F
        self.accumulator = result
        if( not NF):
            self.update_flags(result, carry=borrow, borrow=int(auxiliary_borrow))
        return result
    def subtract_16(self, operand1, operand2, NF = False):
        result = (operand1 - operand2) & 0xFFFF
        borrow = (operand1 - operand2) < 0
        auxiliary_borrow  = ((operand1 & 0x0F) - (operand2 & 0x0F)) > 0x0F
        self.accumulator = result
        if( not NF):
            self.update_flags(result, carry=borrow, borrow=int(auxiliary_borrow))
        return result
    def and_op(self, operand1, operand2):
        result = operand1 & operand2
        self.accumulator = result
        self.update_flags(result)
        return result

    def or_op(self, operand1, operand2):
        result = operand1 | operand2
        self.accumulator = result
        self.update_flags(result)
        return result

    def xor_op(self, operand1, operand2):
        result = operand1 ^ operand2
        self.accumulator = result
        self.update_flags(result)
        return result

    def not_op(self, operand):
        result = (~operand) & 0xFF
        self.accumulator = result
        self.update_flags(result)
        return result

    def rotate_left(self, operand):
        carry = (operand >> 7) & 0x01
        result = ((operand << 1) | carry) & 0xFF
        self.accumulator = result
        self.update_flags(result, carry=carry)
        return result

    def rotate_right(self, operand):
        carry = operand & 0x01
        result = ((operand >> 1) | (carry << 7)) & 0xFF
        self.accumulator = result
        self.update_flags(result, carry=carry)
        return result

    def swap_nibbles(self, operand):
        result = ((operand & 0x0F) << 4) | ((operand & 0xF0) >> 4)
        self.accumulator = result
        self.update_flags(result)
        return result

    def ral(self, operand):
        S, Z, AC, P, C = self.decode_flag(self.flags.read())
        carry_in = int(C)
        carry_out = (operand >> 7) & 0x01
        result = ((operand << 1) | carry_in) & 0xFF
        self.replace_flag(4, carry_out)
        return result

    def rar(self, operand):
        S, Z, AC, P, C = self.decode_flag(self.flags.read())
        carry_in = int(C)
        carry_out =operand & 0x01
        result = ((operand >> 1) | (carry_in << 7)) & 0xFF
        self.accumulator = result
        self.replace_flag(4, carry_out)
        return result