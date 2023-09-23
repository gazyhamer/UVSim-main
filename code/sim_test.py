from methods import Sim

def main():
    tester = Sim()
    
    program = {i: 0 for i in range(100)}

    program[0] = 10_98      # READ #98
    program[1] = 10_99      # READ #99
    program[2] = 20_97      # LOAD #97
    program[3] = 30_99      # ADD #99
    program[4] = 30_98      # ADD #98
    program[5] = 21_97      # STORE #21
    program[6] = 11_97      # WRITE #97
    program[7] = 43_00      # HALT
    
    tester.memory = program
    
    tester.run()

if __name__ == "__main__":
    main()
