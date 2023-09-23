"""main file for program."""
from methods import Sim
from pathlib import Path
def main():
    """main""" 
    file_path = Path(__file__).with_name('basicMLcode.txt')
    sim = Sim()
    sim.Compiler(file_path)
    sim.run()
    print(sim.accumulator)
    #print(sim.int_or_opcode)
    #for f in sim.memory:
        #print(type(f))
    #for f in sim.int_or_opcode:
        #print(type(f))
    #print(sim.memory)
    #print(sim.int_or_opcode)

if __name__ == "__main__":
    main()
