from .cpu import CPU8085


class Runner:
    def __init__(self, cpu: CPU8085):
        self.cpu = cpu

    def readAddress16(self):
        lower = self.cpu.ram.read(self.cpu.PC.get() +1 )
        higher = self.cpu.ram.read(self.cpu.PC.get() + 2)
        addr = int(f"{higher:02x}{lower:02x}", 16)
        return addr

    def MOV(self, opcode):
        if (opcode == "40"):
            self.cpu.MOV(self.cpu.B, self.cpu.B)

        if (opcode == "41"):
            self.cpu.MOV(self.cpu.B, self.cpu.C)

        if (opcode == "42"):
            self.cpu.MOV(self.cpu.B, self.cpu.D)

        if (opcode == "43"):
            self.cpu.MOV(self.cpu.B, self.cpu.E)

        if (opcode == "44"):
            self.cpu.MOV(self.cpu.B, self.cpu.H)

        if (opcode == "45"):
            self.cpu.MOV(self.cpu.B, self.cpu.L)

        if (opcode == "46"):
            self.cpu.MOV(self.cpu.B, self.cpu.M)

        if (opcode == "47"):
            self.cpu.MOV(self.cpu.B, self.cpu.A)

        if (opcode == "48"):
            self.cpu.MOV(self.cpu.C, self.cpu.B)

        if (opcode == "49"):
            self.cpu.MOV(self.cpu.C, self.cpu.C)

        if (opcode == "4A"):
            self.cpu.MOV(self.cpu.C, self.cpu.D)

        if (opcode == "4B"):
            self.cpu.MOV(self.cpu.C, self.cpu.E)

        if (opcode == "4C"):
            self.cpu.MOV(self.cpu.C, self.cpu.H)

        if (opcode == "4D"):
            self.cpu.MOV(self.cpu.C, self.cpu.L)

        if (opcode == "4E"):
            self.cpu.MOV(self.cpu.C, self.cpu.M)

        if (opcode == "4F"):
            self.cpu.MOV(self.cpu.C, self.cpu.A)

        if (opcode == "50"):
            self.cpu.MOV(self.cpu.D, self.cpu.B)

        if (opcode == "51"):
            self.cpu.MOV(self.cpu.D, self.cpu.C)

        if (opcode == "52"):
            self.cpu.MOV(self.cpu.D, self.cpu.D)

        if (opcode == "53"):
            self.cpu.MOV(self.cpu.D, self.cpu.E)

        if (opcode == "54"):
            self.cpu.MOV(self.cpu.D, self.cpu.H)

        if (opcode == "55"):
            self.cpu.MOV(self.cpu.D, self.cpu.L)

        if (opcode == "56"):
            self.cpu.MOV(self.cpu.D, self.cpu.M)

        if (opcode == "57"):
            self.cpu.MOV(self.cpu.D, self.cpu.A)

        if (opcode == "58"):
            self.cpu.MOV(self.cpu.E, self.cpu.B)

        if (opcode == "59"):
            self.cpu.MOV(self.cpu.E, self.cpu.C)

        if (opcode == "5A"):
            self.cpu.MOV(self.cpu.E, self.cpu.D)

        if (opcode == "5B"):
            self.cpu.MOV(self.cpu.E, self.cpu.E)

        if (opcode == "5C"):
            self.cpu.MOV(self.cpu.E, self.cpu.H)

        if (opcode == "5D"):
            self.cpu.MOV(self.cpu.E, self.cpu.L)

        if (opcode == "5E"):
            self.cpu.MOV(self.cpu.E, self.cpu.M)

        if (opcode == "5F"):
            self.cpu.MOV(self.cpu.E, self.cpu.A)

        if (opcode == "60"):
            self.cpu.MOV(self.cpu.H, self.cpu.B)

        if (opcode == "61"):
            self.cpu.MOV(self.cpu.H, self.cpu.C)

        if (opcode == "62"):
            self.cpu.MOV(self.cpu.H, self.cpu.D)

        if (opcode == "63"):
            self.cpu.MOV(self.cpu.H, self.cpu.E)

        if (opcode == "64"):
            self.cpu.MOV(self.cpu.H, self.cpu.H)

        if (opcode == "65"):
            self.cpu.MOV(self.cpu.H, self.cpu.L)

        if (opcode == "66"):
            self.cpu.MOV(self.cpu.H, self.cpu.M)

        if (opcode == "67"):
            self.cpu.MOV(self.cpu.H, self.cpu.A)

        if (opcode == "68"):
            self.cpu.MOV(self.cpu.L, self.cpu.B)

        if (opcode == "69"):
            self.cpu.MOV(self.cpu.L, self.cpu.C)

        if (opcode == "6A"):
            self.cpu.MOV(self.cpu.L, self.cpu.D)

        if (opcode == "6B"):
            self.cpu.MOV(self.cpu.L, self.cpu.E)

        if (opcode == "6C"):
            self.cpu.MOV(self.cpu.L, self.cpu.H)

        if (opcode == "6D"):
            self.cpu.MOV(self.cpu.L, self.cpu.L)

        if (opcode == "6E"):
            self.cpu.MOV(self.cpu.L, self.cpu.M)

        if (opcode == "6F"):
            self.cpu.MOV(self.cpu.L, self.cpu.A)

        if (opcode == "70"):
            self.cpu.MOV(self.cpu.M, self.cpu.B)

        if (opcode == "71"):
            self.cpu.MOV(self.cpu.M, self.cpu.C)

        if (opcode == "72"):
            self.cpu.MOV(self.cpu.M, self.cpu.D)

        if (opcode == "73"):
            self.cpu.MOV(self.cpu.M, self.cpu.E)

        if (opcode == "74"):
            self.cpu.MOV(self.cpu.M, self.cpu.H)

        if (opcode == "75"):
            self.cpu.MOV(self.cpu.M, self.cpu.L)

        if (opcode == "77"):
            self.cpu.MOV(self.cpu.M, self.cpu.A)

        if (opcode == "78"):
            self.cpu.MOV(self.cpu.A, self.cpu.B)

        if (opcode == "79"):
            self.cpu.MOV(self.cpu.A, self.cpu.C)

        if (opcode == "7A"):
            self.cpu.MOV(self.cpu.A, self.cpu.D)

        if (opcode == "7B"):
            self.cpu.MOV(self.cpu.A, self.cpu.E)

        if (opcode == "7C"):
            self.cpu.MOV(self.cpu.A, self.cpu.H)

        if (opcode == "7D"):
            self.cpu.MOV(self.cpu.A, self.cpu.L)

        if (opcode == "7E"):
            self.cpu.MOV(self.cpu.A, self.cpu.M)

        if (opcode == "7F"):
            self.cpu.MOV(self.cpu.A, self.cpu.A)

    def MVI(self, opcode):
        if (opcode == "06"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.B, operand)

        if (opcode == "0E"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.C, operand)

        if (opcode == "16"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.D, operand)

        if (opcode == "1E"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.E, operand)

        if (opcode == "26"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.H, operand)

        if (opcode == "2E"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.L, operand)

        if (opcode == "36"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.M, operand)

        if (opcode == "3E"):
            operand = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.MVI(self.cpu.A, operand)

    def LDAX(self, opcode):
        if opcode == "0A":
            self.cpu.LDAX(self.cpu.BC)
        if opcode == "1A":
            self.cpu.LDAX(self.cpu.DE)

    def LHLD(self, opcode):
        if opcode == "2A":
            addr = self.readAddress16()
            self.cpu.LHLD(addr)

    def LDA(self, opcode):
        if opcode == "3A":
            addr = self.readAddress16()
            self.cpu.LDA(addr)

    def STAX(self, opcode):
        if opcode == "02":
            self.cpu.STAX(self.cpu.BC)
        if opcode == "12":
            self.cpu.STAX(self.cpu.DE)

    def SHLD(self, opcode):
        if opcode == "22":
            addr = self.readAddress16()
            self.cpu.SHLD(addr)

    def STA(self, opcode):
        if opcode == "32":
            addr = self.readAddress16()
            self.cpu.STA(addr)

    def LXI(self, opcode):
        addr = self.readAddress16()
        if (opcode == "01"):
            self.cpu.LXI(self.cpu.BC, addr)

        if (opcode == "11"):
            self.cpu.LXI(self.cpu.DE, addr)

        if (opcode == "21"):
            self.cpu.LXI(self.cpu.HL, addr)

        if (opcode == "31"):
            self.cpu.LXI(self.cpu.SP, addr)

    def SPHL(self, opcode):
        if opcode == "F9":
            self.cpu.SPHL()

    def XTHL(self, opcode):
        if opcode == "EE":
            self.cpu.XTHL()

    def XCHG(self, opcode):
        if opcode == "EB":
            self.cpu.XCHG()

    def OUT(self, opcode):
        if opcode == "D3":
            port = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.OUT(port)

    def IN(self, opcode):
        if opcode == "DB":
            port = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.IN(port)

    def PUSH(self, opcode):
        if opcode == "C5":
            self.cpu.PUSH(self.cpu.BC)
        if opcode == "D5":
            self.cpu.PUSH(self.cpu.DE)
        if opcode == "E5":
            self.cpu.PUSH(self.cpu.HL)
        if opcode == "F5":
            self.cpu.PUSH(self.cpu.PSW)

    def POP(self, opcode):
        if opcode == "C1":
            self.cpu.POP(self.cpu.BC)
        if opcode == "D1":
            self.cpu.POP(self.cpu.DE)
        if opcode == "E1":
            self.cpu.POP(self.cpu.HL)
        if opcode == "F1":
            self.cpu.POP(self.cpu.PSW)

    def ADD(self, opcode):
        if opcode == "80":
            self.cpu.ADD(self.cpu.B)
        if opcode == "81":
            self.cpu.ADD(self.cpu.C)
        if opcode == "82":
            self.cpu.ADD(self.cpu.D)
        if opcode == "83":
            self.cpu.ADD(self.cpu.E)
        if opcode == "84":
            self.cpu.ADD(self.cpu.H)
        if opcode == "85":
            self.cpu.ADD(self.cpu.L)
        if opcode == "86":
            self.cpu.ADD(self.cpu.M)
        if opcode == "87":
            self.cpu.ADD(self.cpu.A)

    def ADC(self, opcode):
        if opcode == "88":
            self.cpu.ADC(self.cpu.B)
        if opcode == "89":
            self.cpu.ADC(self.cpu.C)
        if opcode == "8A":
            self.cpu.ADC(self.cpu.D)
        if opcode == "8B":
            self.cpu.ADC(self.cpu.E)
        if opcode == "8C":
            self.cpu.ADC(self.cpu.H)
        if opcode == "8D":
            self.cpu.ADC(self.cpu.L)
        if opcode == "8E":
            self.cpu.ADC(self.cpu.M)
        if opcode == "8F":
            self.cpu.ADC(self.cpu.A)

    def ADI(self, opcode):
        if opcode == "C6":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.ADI(data)

    def ACI(self, opcode):
        if opcode == "CE":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.ACI(data)

    def SUB(self, opcode):
        if opcode == "90":
            self.cpu.SUB(self.cpu.B)
        if opcode == "91":
            self.cpu.SUB(self.cpu.C)
        if opcode == "92":
            self.cpu.SUB(self.cpu.D)
        if opcode == "93":
            self.cpu.SUB(self.cpu.E)
        if opcode == "94":
            self.cpu.SUB(self.cpu.H)
        if opcode == "95":
            self.cpu.SUB(self.cpu.L)
        if opcode == "96":
            self.cpu.SUB(self.cpu.M)
        if opcode == "97":
            self.cpu.SUB(self.cpu.A)

    def SBB(self, opcode):
        if opcode == "98":
            self.cpu.SBB(self.cpu.B)
        if opcode == "99":
            self.cpu.SBB(self.cpu.C)
        if opcode == "9A":
            self.cpu.SBB(self.cpu.D)
        if opcode == "9B":
            self.cpu.SBB(self.cpu.E)
        if opcode == "9C":
            self.cpu.SBB(self.cpu.H)
        if opcode == "9D":
            self.cpu.SBB(self.cpu.L)
        if opcode == "9E":
            self.cpu.SBB(self.cpu.M)
        if opcode == "9F":
            self.cpu.SBB(self.cpu.A)

    def SUI(self, opcode):
        if opcode == "D6":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.SUI(data)

    def SBI(self, opcode):
        if opcode == "DE":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.SBI(data)

    def DAD(self, opcode):
        if opcode == "09":
            self.cpu.DAD(self.cpu.BC)
        if opcode == "19":
            self.cpu.DAD(self.cpu.DE)
        if opcode == "29":
            self.cpu.DAD(self.cpu.HL)
        if opcode == "39":
            self.cpu.DAD(self.cpu.SP)

    def DAA(self, opcode):
        if opcode == "27":
            self.cpu.DAA()

    def INR(self, opcode):
        if opcode == "04":
            self.cpu.INR(self.cpu.B)
        if opcode == "0C":
            self.cpu.INR(self.cpu.C)
        if opcode == "14":
            self.cpu.INR(self.cpu.D)
        if opcode == "1C":
            self.cpu.INR(self.cpu.E)
        if opcode == "24":
            self.cpu.INR(self.cpu.H)
        if opcode == "2C":
            self.cpu.INR(self.cpu.L)
        if opcode == "34":
            self.cpu.INR(self.cpu.M)
        if opcode == "3C":
            self.cpu.INR(self.cpu.A)

    def INX(self, opcode):
        if opcode == "03":
            self.cpu.INX(self.cpu.BC)
        if opcode == "13":
            self.cpu.INX(self.cpu.DE)
        if opcode == "23":
            self.cpu.INX(self.cpu.HL)
        if opcode == "33":
            self.cpu.INX(self.cpu.SP)

    def DCR(self, opcode):
        if opcode == "05":
            self.cpu.DCR(self.cpu.B)
        if opcode == "0D":
            self.cpu.DCR(self.cpu.C)
        if opcode == "15":
            self.cpu.DCR(self.cpu.D)
        if opcode == "1D":
            self.cpu.DCR(self.cpu.E)
        if opcode == "25":
            self.cpu.DCR(self.cpu.H)
        if opcode == "2D":
            self.cpu.DCR(self.cpu.L)
        if opcode == "35":
            self.cpu.DCR(self.cpu.M)
        if opcode == "3D":
            self.cpu.DCR(self.cpu.A)

    def DCX(self, opcode):
        if opcode == "0B":
            self.cpu.DCX(self.cpu.BC)
        if opcode == "1B":
            self.cpu.DCX(self.cpu.DE)
        if opcode == "2B":
            self.cpu.DCX(self.cpu.HL)
        if opcode == "3B":
            self.cpu.DCX(self.cpu.SP)

    def STC(self, opcode):
        if opcode == "37":
            self.cpu.STC()

    def ANA(self, opcode):
        if opcode == "A0":
            self.cpu.ANA(self.cpu.B)
        if opcode == "A1":
            self.cpu.ANA(self.cpu.C)
        if opcode == "A2":
            self.cpu.ANA(self.cpu.D)
        if opcode == "A3":
            self.cpu.ANA(self.cpu.E)
        if opcode == "A4":
            self.cpu.ANA(self.cpu.H)
        if opcode == "A5":
            self.cpu.ANA(self.cpu.L)
        if opcode == "A6":
            self.cpu.ANA(self.cpu.M)
        if opcode == "A7":
            self.cpu.ANA(self.cpu.A)

    def ANI(self, opcode):
        if opcode == "E6":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.ANI(data)

    def XRA(self, opcode):
        if opcode == "A8":
            self.cpu.XRA(self.cpu.B)
        if opcode == "A9":
            self.cpu.XRA(self.cpu.C)
        if opcode == "AA":
            self.cpu.XRA(self.cpu.D)
        if opcode == "AB":
            self.cpu.XRA(self.cpu.E)
        if opcode == "AC":
            self.cpu.XRA(self.cpu.H)
        if opcode == "AD":
            self.cpu.XRA(self.cpu.L)
        if opcode == "AE":
            self.cpu.XRA(self.cpu.M)
        if opcode == "AF":
            self.cpu.XRA(self.cpu.A)

    def XRI(self, opcode):
        if opcode == "EE":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.XRI(data)

    def ORA(self, opcode):
        if opcode == "B0":
            self.cpu.ORA(self.cpu.B)
        if opcode == "B1":
            self.cpu.ORA(self.cpu.C)
        if opcode == "B2":
            self.cpu.ORA(self.cpu.D)
        if opcode == "B3":
            self.cpu.ORA(self.cpu.E)
        if opcode == "B4":
            self.cpu.ORA(self.cpu.H)
        if opcode == "B5":
            self.cpu.ORA(self.cpu.L)
        if opcode == "B6":
            self.cpu.ORA(self.cpu.M)
        if opcode == "B7":
            self.cpu.ORA(self.cpu.A)

    def ORI(self, opcode):
        if opcode == "F6":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.ORI(data)

    def CMP(self, opcode):
        if opcode == "B8":
            self.cpu.CMP(self.cpu.B)
        if opcode == "B9":
            self.cpu.CMP(self.cpu.C)
        if opcode == "BA":
            self.cpu.CMP(self.cpu.D)
        if opcode == "BB":
            self.cpu.CMP(self.cpu.E)
        if opcode == "BC":
            self.cpu.CMP(self.cpu.H)
        if opcode == "BD":
            self.cpu.CMP(self.cpu.L)
        if opcode == "BE":
            self.cpu.CMP(self.cpu.M)
        if opcode == "BF":
            self.cpu.CMP(self.cpu.A)

    def CPI(self, opcode):
        if opcode == "FE":
            data = self.cpu.ram.read(self.cpu.PC.get() + 1)
            self.cpu.CPI(data)

    def RLC(self, opcode):
        if opcode == "07":
            self.cpu.RLC()

    def RRC(self, opcode):
        if opcode == "0F":
            self.cpu.RRC()

    def RAL(self, opcode):
        if opcode == "17":
            self.cpu.RAL()

    def RAR(self, opcode):
        if opcode == "1F":
            self.cpu.RAR()

    def CMA(self, opcode):
        if opcode == "2F":
            self.cpu.CMA()

    def CMC(self, opcode):
        if opcode == "3F":
            self.cpu.CMC()

    def JMP(self, opcode):

        if opcode == "C3":
            addr = self.readAddress16()
            self.cpu.JMP(addr)


    def JC(self, opcode):
        if opcode == "DA":
            addr = self.readAddress16()
            self.cpu.JC(addr)

    def JNC(self, opcode):
        if opcode == "D2":
            addr = self.readAddress16()
            self.cpu.JNC(addr)

    def JP(self, opcode):
        if opcode == "F2":
            addr = self.readAddress16()
            self.cpu.JP(addr)

    def JM(self, opcode):
        if opcode == "FA":
            addr = self.readAddress16()
            self.cpu.JM(addr)

    def JPE(self, opcode):
        if opcode == "EA":
            addr = self.readAddress16()
            self.cpu.JPE(addr)

    def JPO(self, opcode):
        if opcode == "E2":
            addr = self.readAddress16()
            self.cpu.JPO(addr)

    def JZ(self, opcode):
        if opcode == "CA":
            addr = self.readAddress16()
            self.cpu.JZ(addr)

    def JNZ(self, opcode):
        if opcode == "C2":
            addr = self.readAddress16()
            self.cpu.JNZ(addr)

    def PCHL(self, opcode):
        if opcode == "E9":
            self.cpu.PCHL()

    def RST(self, opcode):
        if opcode == "C7":
            self.cpu.RST(0)
        if opcode == "CF":
            self.cpu.RST(1)
        if opcode == "D7":
            self.cpu.RST(2)
        if opcode == "DF":
            self.cpu.RST(3)
        if opcode == "E7":
            self.cpu.RST(4)
        if opcode == "EF":
            self.cpu.RST(5)
        if opcode == "F7":
            self.cpu.RST(6)
        if opcode == "FF":
            self.cpu.RST(7)

    def CALL(self, opcode):
        if opcode == "CD":
            addr = self.readAddress16()
            self.cpu.CALL(addr)

    def CC(self, opcode):
        if opcode == "DC":
            addr = self.readAddress16()
            self.cpu.CC(addr)

    def CNC(self, opcode):
        if opcode == "D4":
            addr = self.readAddress16()
            self.cpu.CNC(addr)

    def CP(self, opcode):
        if opcode == "F4":
            addr = self.readAddress16()
            self.cpu.CP(addr)

    def CM(self, opcode):
        if opcode == "FC":
            addr = self.readAddress16()
            self.cpu.CM(addr)

    def CPE(self, opcode):
        if opcode == "EC":
            addr = self.readAddress16()
            self.cpu.CPE(addr)

    def CPO(self, opcode):
        if opcode == "E4":
            addr = self.readAddress16()
            self.cpu.CPO(addr)

    def CZ(self, opcode):
        if opcode == "CC":
            addr = self.readAddress16()
            self.cpu.CZ(addr)

    def CNZ(self, opcode):
        if opcode == "C4":
            addr = self.readAddress16()
            self.cpu.CNZ(addr)

    def RET(self, opcode):
        if opcode == "C9":
            self.cpu.RET()

    def RC(self, opcode):
        if opcode == "D8":
            self.cpu.RC()

    def RNC(self, opcode):
        if opcode == "D0":
            self.cpu.RNC()

    def RP(self, opcode):
        if opcode == "F0":
            self.cpu.RP()

    def RM(self, opcode):
        if opcode == "F8":
            self.cpu.RM()

    def RPE(self, opcode):
        if opcode == "E8":
            self.cpu.RPE()

    def RPO(self, opcode):
        if opcode == "E0":
            self.cpu.RPO()

    def RZ(self, opcode):
        if opcode == "C8":
            self.cpu.RZ()

    def RNZ(self, opcode):
        if opcode == "C0":
            self.cpu.RNZ()

    def NOP(self, opcode):
        if opcode == "00":
            self.cpu.NOP()

    def HLT(self, opcode):
        if opcode == "76":
            self.cpu.HLT()

    def DI(self, opcode):
        if opcode == "F3":
            self.cpu.DI()

    def EI(self, opcode):
        if opcode == "FB":
            self.cpu.EI()

    def RIM(self, opcode):
        if opcode == "20":
            self.cpu.RIM()

    def SIM(self, opcode):
        if opcode == "30":
            self.cpu.SIM()