from MP8085.simulator import Simulator
from MP8085.compiler import compile
def h(val):
    return int(f"{val}", 16)

sim = Simulator()
st = h("0800")
source = open("test.asm", "r").read()


code = compile(source, start_address=st)
sim.load(st, code)

sim.run()

sim.cpu.ram.dump_to_file("ram.bin")

