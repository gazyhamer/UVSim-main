"""methods go here when we do them? Unless someone
has a different idea, this is what I'm starting with."""



class Sim:
    '''this is the simulated object to use as the cpu/insides 
    of the sim, like the lc3'''
    def __init__(self):
        self.accumulator = None
        self.memory = dict.fromkeys(range(0,100),0)
        #zero would indicate and integer
        self.int_or_opcode = dict.fromkeys(range(0,100),0)
            # using a dict might be easier to control since a list of 
            # 100 might be added to accidentally more easily than a dict.
            # Just a thought.
        self.counter = 0
            # counter that the sim can use to move through its memory,
            # we need something for the control operations to point to
          
        # Numerical codes for each function from requirements.  
        self.op_codes = {
            10: self.read,
            11: self.write,
            
            20: self.load,
            21: self.store,
            
            30: self.add,
            31: self.subtract,
            32: self.divide,
            33: self.multiply,
            
            40: self.branch,
            41: self.branch_neg,
            42: self.branch_zero
        }

    def run(self, start_address = 0) -> None:
        """Run current memory from given start address"""
        self.counter = start_address
        
        while self.counter < len(self.memory):
            current_code = self.int_or_opcode[self.counter]
            #print(self.int_or_opcode[self.counter])
            current_input = self.memory[self.counter]
            
            # Special case for Halt.
            if current_code == 43:
                break
            if current_code in self.op_codes:
                self.op_codes[current_code](current_input)
            self.counter += 1

    """Read a word from the keyboard into a specific location in memory."""
    def read(self, location):
        try:
            input_value = int(input("Enter a word: "))
            self.memory[location] = input_value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    """Write a word from a specific location in memory to screen."""
    def write(self, location):
        print(f"Word at location {location}: {self.memory[location]}")

    """Load a word from a specific location in memory into the accumulator."""
    def load(self, location):
        self.accumulator = self.memory[location]

    """Store a word from the accumulator into a specific location in memory."""
    def store(self, location):
        self.memory[location] = self.accumulator


    # arithmetic operatior
    """Helper functions to handle overflow"""
    def overflow_handling(self, overflow_number):
        while overflow_number > 9999 or overflow_number < -9999:
                if overflow_number < -9999:
                    overflow_number += 19999
                else:
                    overflow_number -= 19999
        return overflow_number

    """ Add a word from a specific location in memory to the word in the
        accumulator (leave the result in the accumulator)"""
    def add(self, location):
        #placeholder is to decide whether the number is acceptilbe to fit in the accumulator
        placeholder = self.accumulator + self.memory[location]
        """if the placeholder is within the four diget signed interger it will be placed in
        if not it will be sent to the overflow helper function"""
        if placeholder <= 9999 and placeholder >= -9999:
            self.accumulator = placeholder
        else:
            self.accumulator = self.overflow_handling(placeholder)

    """Subtract a word from a specific location in memory from the word in the
      accumulator (leave the result in the accumulator)"""
    def subtract(self, location):
        placeholder = self.accumulator - self.memory[location]
        """if the placeholder is within the four diget signed interger it will be placed in
        if not it will be sent to the overflow helper function"""
        if placeholder <= 9999 and placeholder >= -9999:
            self.accumulator = placeholder
        else:
            self.accumulator = self.overflow_handling(placeholder)
    
    """ Divide the word in the accumulator by a word from a specific
      location in memory (leave the result in the accumulator)."""
    def divide(self, location):
        # This if statement handles divide by zero returning zero
        if(self.memory[location]==0):
            return 0
        placeholder = self.accumulator / self.memory[location]
        """if the placeholder is within the four diget signed interger it will be placed in
        if not it will be sent to the overflow helper function"""
        if placeholder <= 9999 and placeholder >= -9999:
            self.accumulator = placeholder
        else:
            self.accumulator = int(round(self.overflow_handling(placeholder)))
    
    """multiply a word from a specific location in memory to the word 
    in the accumulator (leave the result in the accumulator)."""
    def multiply(self,location):
        placeholder = self.accumulator * self.memory[location]
        """if the placeholder is within the four diget signed interger it will be placed in
        if not it will be sent to the overflow helper function"""
        if placeholder <= 9999 and placeholder >= -9999:
            self.accumulator = placeholder
        else:
            self.accumulator = int(self.overflow_handling(placeholder))
            print(self.accumulator)


    # control operations - evin
    def branch(self, location):
        """moves the sim pointer to a spot in the memory"""
        self.counter = location -1

    def branch_neg(self, location):
        """moves the sim pointer to a spot in the memory
        only if accumulator is negative"""
        if self.accumulator is not None and self.accumulator < 0:
            self.counter = location - 1

    def branch_zero(self, location):
        """moves the sim pointer to a spot in the memory
        only if accumulator is zero"""
        if self.accumulator is not None and self.accumulator == 0:
            self.counter = location -1

    #Compiler
    """Helper functions takes a string and changes it to opcode value"""
    def string_to_opcode(self, string):
        string = string.lower()
        opcode = {
                "read" : "10_",
                "write" : "11_",
                "load" : "20_",
                "store" : "21_",
                "add" : "30_",
                "subtract" : "31_",
                "divide" : "32_",
                "multiply" : "33_",
                "branch" : "40_",
                "branch_neg" : "41_",
                "branch_zero" : "42_"
            }
        if string in opcode.keys():
            return opcode[string]
        else:
            return string
    
    """Takes a file reads in the contents to memory to run program"""
    def Compiler(self, filename):
        memory_location = 0
        with open(filename,'r') as file:
            for line in file:
                #checks the line is blank or is commented out
                if '#' in line or line.strip() == '':
                    pass
                else:
                    #formats the input file from a string to an integer
                    line = line.split()
                    line[0] = self.string_to_opcode(line[0])
                    if '_' in line[0]:
                        self.int_or_opcode[memory_location] = int(line[0][0:2])
                        self.memory[memory_location] = int(line[1])
                        memory_location += 1
                    elif line != []:
                        try:
                            self.memory[memory_location] = int(line[0])
                            memory_location += 1
                        except ValueError:
                            print(f"failed to compile {line} is not a integer")
        file.close()