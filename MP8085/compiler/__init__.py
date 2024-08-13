from .Codes import *
cmd_8085 = {"label" : None,
            "opcode" : "",
            "operands": None}

def parse_8085_asm_line(line) -> dict:
    ret = {"label": None, "opcode": "", "operands": None}
    code = line

    if ":" in line:
        label = line.split(":")
        code = label[1].strip()
        ret["label"] = label[0].strip()

    if ";" in code:
        code = code.split(";")[0].strip()

    if " " in code:
        data = code.split(" ", 1)
        ret["opcode"] = data[0].strip().upper()
        ret["operands"] = [operand.strip() if operand.strip().lower() == "h" else operand.strip().replace('h', '').replace('H', '') for operand in data[1].split(",")]
    else:
        ret["opcode"] = code.strip().upper()
        ret["operands"] = []

    return ret


def call_instruction(cmd_8085: dict) -> str:
    opcode = cmd_8085["opcode"].upper()
    operands = cmd_8085["operands"]

    if opcode == "ACI":
        return ACI(int(operands[0], 16))
    elif opcode == "ADC":
        return ADC(operands[0])
    elif opcode == "ADD":
        return ADD(operands[0])
    elif opcode == "ADI":
        return ADI(int(operands[0], 16))
    elif opcode == "ANA":
        return ANA(operands[0])
    elif opcode == "ANI":
        return ANI(int(operands[0], 16))
    elif opcode == "CALL":
        return CALL(int(operands[0], 16))
    elif opcode == "CMA":
        return CMA()
    elif opcode == "CMC":
        return CMC()
    elif opcode == "CMP":
        return CMP(operands[0])
    elif opcode == "CPI":
        return CPI(int(operands[0], 16))
    elif opcode == "DAA":
        return DAA()
    elif opcode == "DAD":
        return DAD(operands[0])
    elif opcode == "DCR":
        return DCR(operands[0])
    elif opcode == "DCX":
        return DCX(operands[0])
    elif opcode == "DI":
        return DI()
    elif opcode == "EI":
        return EI()
    elif opcode == "HLT":
        return HLT()
    elif opcode == "IN":
        return IN(int(operands[0], 16))
    elif opcode == "INR":
        return INR(operands[0])
    elif opcode == "INX":
        return INX(operands[0])
    elif opcode == "JMP":
        return JMP(int(operands[0], 16))
    elif opcode == "JC":
        return JC(int(operands[0], 16))
    elif opcode == "JNC":
        return JNC(int(operands[0], 16))
    elif opcode == "JP":
        return JP(int(operands[0], 16))
    elif opcode == "JM":
        return JM(int(operands[0], 16))
    elif opcode == "JPE":
        return JPE(int(operands[0], 16))
    elif opcode == "JPO":
        return JPO(int(operands[0], 16))
    elif opcode == "JZ":
        return JZ(int(operands[0], 16))
    elif opcode == "JNZ":
        return JNZ(int(operands[0], 16))
    elif opcode == "LDA":
        return LDA(int(operands[0], 16))
    elif opcode == "LDAX":
        return LDAX(operands[0])
    elif opcode == "LHLD":
        return LHLD(int(operands[0], 16))
    elif opcode == "LXI":
        return LXI(operands[0], int(operands[1], 16))
    elif opcode == "MOV":
        return MOV(operands[0], operands[1])
    elif opcode == "MVI":
        return MVI(operands[0], int(operands[1].replace('H', ''), 16))
    elif opcode == "NOP":
        return NOP()
    elif opcode == "ORA":
        return ORA(operands[0])
    elif opcode == "ORI":
        return ORI(int(operands[0], 16))
    elif opcode == "OUT":
        return OUT(int(operands[0], 16))
    elif opcode == "PCHL":
        return PCHL()
    elif opcode == "POP":
        return POP(operands[0])
    elif opcode == "PUSH":
        return PUSH(operands[0])
    elif opcode == "RAL":
        return RAL()
    elif opcode == "RAR":
        return RAR()
    elif opcode == "RLC":
        return RLC()
    elif opcode == "RRC":
        return RRC()
    elif opcode == "RET":
        return RET()
    elif opcode == "RC":
        return RC()
    elif opcode == "RNC":
        return RNC()
    elif opcode == "RP":
        return RP()
    elif opcode == "RM":
        return RM()
    elif opcode == "RPE":
        return RPE()
    elif opcode == "RPO":
        return RPO()
    elif opcode == "RZ":
        return RZ()
    elif opcode == "RNZ":
        return RNZ()
    elif opcode == "RIM":
        return RIM()
    elif opcode == "RST":
        return RST(int(operands[0]))
    elif opcode == "SBB":
        return SBB(operands[0])
    elif opcode == "SBI":
        return SBI(int(operands[0], 16))
    elif opcode == "SHLD":
        return SHLD(int(operands[0], 16))
    elif opcode == "SIM":
        return SIM()
    elif opcode == "SPHL":
        return SPHL()
    elif opcode == "STA":
        return STA(int(operands[0], 16))
    elif opcode == "STAX":
        return STAX(operands[0])
    elif opcode == "STC":
        return STC()
    elif opcode == "SUB":
        return SUB(operands[0])
    elif opcode == "SUI":
        return SUI(int(operands[0], 16))
    elif opcode == "XCHG":
        return XCHG()
    elif opcode == "XRA":
        return XRA(operands[0])
    elif opcode == "XRI":
        return XRI(int(operands[0], 16))
    elif opcode == "XTHL":
        return XTHL()
    else:
        raise ValueError(f"Instruction '{opcode}' not found.")


def instruction_size(instruction):
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
    return sizes.get(instruction.upper(), "Invalid instruction")
def parse_code(code : str, start_address):
    at = 0
    addr = start_address

    new_code = []

    label_calls = []
    label_address = {}

    for k in code.split("\n"):
        i = k.strip()
        if(i == ""):
            continue

        instructions = {
            "JMP",
            "JZ",
            "JNZ",
            "JC",
            "JNC",
            "JP",
            "JM",
            "JPE",
            "JPO",
            "CALL",
            "CZ",
            "CNZ",
            "CC",
            "CNC",
            "CP",
            "CM",
            "CPE",
            "CPO"
        }
        ins = parse_8085_asm_line(i)
        new_code.append(ins)

        if(ins["label"] != None):
            label_address[ins["label"]] = f"{addr:#06x}".split("x")[1]

        if(ins["opcode"] in instructions):
            label_calls.append(at)


        at += 1
        addr += instruction_size(ins["opcode"].strip())

    for i in label_calls:
        try :
            if int((new_code[i]["operands"][0]), 16):
                pass
        except:
            new_code[i]["operands"][0] = (label_address[new_code[i]["operands"][0]])


    code = ""
    for i in new_code:
        opcode = i["opcode"]
        operands = i["operands"]

        thisLine = opcode + " " + ", ".join(operands)
        code += thisLine + "\n"
    return code

def compile(code, start_address = 0x0000, save = None):
    compiled_byes = ""

    processed_source = parse_code(code.strip(), start_address)
    for i in processed_source.strip().split("\n"):
        if(i.strip() == ""):
            continue
        compiled_byes += (call_instruction(parse_8085_asm_line(i.strip()))) + " "

    if(save != None):
        byte_data = bytes.fromhex(compiled_byes)
        file_path = save
        with open(file_path, 'wb') as binary_file:
            binary_file.write(byte_data)

    return compiled_byes

