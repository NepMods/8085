import os
import time

from .cpu import CPU8085
from .Runner import Runner
class Simulator:
    def __init__(self):
        self.cpu = CPU8085()
        self.runner = Runner(self.cpu)

    def load(self, at, bytes):
        if (os.path.exists("ram.d")):
            def h(val):
                return int(f"{val}", 16)

            ram_default = open("ram.d", "r").readlines()
            for i in ram_default:
                self.cpu.ram.write(h(i.split("=")[0].strip()), h(i.split("=")[1].strip()))

        self.at = at
        addr = at
        for i in bytes.strip().split(" "):
            self.cpu.ram.write(addr, int(i, 16))
            addr += 0x1

        self.set_PC(at)
    def loadFile(self, at, filename):
        with open(filename, 'rb') as file:
            byte_data = file.read()

        hex_data = ' '.join(f'{byte:02X}' for byte in byte_data)
        self.load(at, hex_data)

    def run(self):
        end = 0
        o = ""
        self.cpu.SP.set(int("FFFF", 16))
        while(not end):

            byte = self.cpu.ram.read(self.cpu.PC.read())
            o_hex = f"{byte:02X}"
            operation = self.cpu.operations[o_hex]
            name =operation["opcode"]
            size = self.cpu.getSize(name)
            opcode = o_hex


            if (operation["opcode"] == "MOV"):
                self.runner.MOV(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "MVI"):
                self.runner.MVI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "LDAX"):
                self.runner.LDAX(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "LHLD"):
                self.runner.LHLD(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "LDA"):
                self.runner.LDA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "STAX"):
                self.runner.STAX(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SHLD"):
                self.runner.SHLD(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "STA"):
                self.runner.STA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "LXI"):
                self.runner.LXI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SPHL"):
                self.runner.SPHL(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "XTHL"):
                self.runner.XTHL(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "XCHG"):
                self.runner.XCHG(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "OUT"):
                self.runner.OUT(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "IN"):
                self.runner.IN(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "PUSH"):
                self.runner.PUSH(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "POP"):
                self.runner.POP(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ADD"):
                self.runner.ADD(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ADC"):
                self.runner.ADC(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ADI"):
                self.runner.ADI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ACI"):
                self.runner.ACI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SUB"):
                self.runner.SUB(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SBB"):
                self.runner.SBB(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SUI"):
                self.runner.SUI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SBI"):
                self.runner.SBI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "DAD"):
                self.runner.DAD(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "DAA"):
                self.runner.DAA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "INR"):
                self.runner.INR(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "INX"):
                self.runner.INX(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "DCR"):
                self.runner.DCR(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "DCX"):
                self.runner.DCX(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "STC"):
                self.runner.STC(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ANA"):
                self.runner.ANA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ANI"):
                self.runner.ANI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "XRA"):
                self.runner.XRA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "XRI"):
                self.runner.XRI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ORA"):
                self.runner.ORA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "ORI"):
                self.runner.ORI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "CMP"):
                self.runner.CMP(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "CPI"):
                self.runner.CPI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "RLC"):
                self.runner.RLC(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "RRC"):
                self.runner.RRC(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "RAL"):
                self.runner.RAL(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "RAR"):
                self.runner.RAR(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "CMA"):
                self.runner.CMA(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "CMC"):
                self.runner.CMC(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "JMP"):
                self.runner.JMP(opcode)

            if (operation["opcode"] == "JC"):
                self.runner.JC(opcode)

            if (operation["opcode"] == "JNC"):
                self.runner.JNC(opcode)

            if (operation["opcode"] == "JP"):
                self.runner.JP(opcode)

            if (operation["opcode"] == "JM"):
                self.runner.JM(opcode)

            if (operation["opcode"] == "JPE"):
                self.runner.JPE(opcode)

            if (operation["opcode"] == "JPO"):
                self.runner.JPO(opcode)

            if (operation["opcode"] == "JZ"):
                self.runner.JZ(opcode)

            if (operation["opcode"] == "JNZ"):
                self.runner.JNZ(opcode)

            if (operation["opcode"] == "PCHL"):
                self.runner.PCHL(opcode)

            if (operation["opcode"] == "RST"):
                self.runner.RST(opcode)

            if (operation["opcode"] == "CALL"):
                self.runner.CALL(opcode)

            if (operation["opcode"] == "CC"):
                self.runner.CC(opcode)

            if (operation["opcode"] == "CNC"):
                self.runner.CNC(opcode)

            if (operation["opcode"] == "CP"):
                self.runner.CP(opcode)

            if (operation["opcode"] == "CM"):
                self.runner.CM(opcode)

            if (operation["opcode"] == "CPE"):
                self.runner.CPE(opcode)

            if (operation["opcode"] == "CPO"):
                self.runner.CPO(opcode)

            if (operation["opcode"] == "CZ"):
                self.runner.CZ(opcode)

            if (operation["opcode"] == "CNZ"):
                self.runner.CNZ(opcode)

            if (operation["opcode"] == "RET"):
                self.runner.RET(opcode)

            if (operation["opcode"] == "RC"):
                self.runner.RC(opcode)

            if (operation["opcode"] == "RNC"):
                self.runner.RNC(opcode)

            if (operation["opcode"] == "RP"):
                self.runner.RP(opcode)

            if (operation["opcode"] == "RM"):
                self.runner.RM(opcode)

            if (operation["opcode"] == "RPE"):
                self.runner.RPE(opcode)

            if (operation["opcode"] == "RPO"):
                self.runner.RPO(opcode)

            if (operation["opcode"] == "RZ"):
                self.runner.RZ(opcode)

            if (operation["opcode"] == "RNZ"):
                self.runner.RNZ(opcode)

            if (operation["opcode"] == "NOP"):
                self.runner.NOP(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "HLT"):
                self.runner.HLT(opcode)
                end = 1

            if (operation["opcode"] == "DI"):
                self.runner.DI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "EI"):
                self.runner.EI(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "RIM"):
                self.runner.RIM(opcode)
                self.increase_PC(size)

            if (operation["opcode"] == "SIM"):
                self.runner.SIM(opcode)
                self.increase_PC(size)

    def set_PC(self, address):
        data = int(f"{address:04X}", 16)
        self.cpu.PC.write(data)

    def increase_PC(self, by):
        data = int(f"{self.cpu.PC.read():04X}", 16)
        self.cpu.PC.write(data + by)

