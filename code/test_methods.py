"""file for test cases"""


import methods


# test system object creation
new_system = methods.Sim()

def test_system_creation_accum():
    """test accumulator creation"""
    assert new_system.accumulator is None

def test_system_creation_counter():
    """test counter creation"""
    assert new_system.counter == 0

def test_system_creation_mem():
    """test memory creation"""
    assert len(new_system.memory) == 100
    assert new_system.memory[33] is None


# test IO methods
# Read 
new_system.read(0)
assert type(new_system.memory[0]) == int

# Write
new_system.write(0)

# test load/store methods
# Load
new_system.memory[0] = 5
new_system.load(0)
assert new_system.accumulator == 5

# Store
new_system.store(1)
assert new_system.memory[1] == 5

# test arithmetic methods
# Addition
assert new_system.accumulator == 5
new_system.accumulator = 1
new_system.memory[0] = 9999
new_system.add(0)

assert new_system.accumulator == -9999
new_system.accumulator = -1
new_system.memory[0] = -9999
new_system.add(0)
assert new_system.accumulator == 9999

new_system.memory[1] = 4526
new_system.add(1)
assert new_system.accumulator == -5474

# Subtraction
new_system.accumulator = -9999
new_system.memory[0] = 1
new_system.subtract(0)
assert new_system.accumulator == 9999

new_system.memory[0] = -1
new_system.subtract(0)
assert new_system.accumulator == -9999

new_system.memory[0] = 4526
new_system.subtract(0)
assert new_system.accumulator == 5474

# Divsion
new_system.accumulator = 100
new_system.memory[0] = 5
new_system.divide(0)
assert new_system.accumulator == 20

# Multiplication
new_system.multiply(0)
assert new_system.accumulator == 100

# test control methods
def test_branch():
    """test branch method"""
    sim_4 = methods.Sim()
    assert sim_4.counter == 0
    sim_4.branch(33)
    assert sim_4.counter == 33

def test_branch_neg():
    """test branch_neg method with all possible options"""
    sim_4 = methods.Sim()
    #  test with accumulator at None
    sim_4.branch_neg(33)
    assert sim_4.counter == 0
    # test with accumulator at positive
    sim_4.accumulator = 1
    sim_4.branch_neg(33)
    assert sim_4.counter == 0
    # test with accumulator at negative
    sim_4.accumulator = -3
    sim_4.branch_neg(33)
    assert sim_4.counter == 33

def test_branch_zero():
    """test branch_zero with all possible options"""
    sim_4 = methods.Sim()
    # test with accumulator at None
    sim_4.branch_zero(33)
    assert sim_4.counter == 0
    # test with accumulator positive
    sim_4.accumulator = 1
    sim_4.branch_zero(33)
    assert sim_4.counter == 0
    # test with accumulator at negative
    sim_4.accumulator = -3
    sim_4.branch_zero(33)
    assert sim_4.counter == 0
    # test with accumulator at 0
    sim_4.accumulator = 0
    sim_4.branch_zero(33)
    assert sim_4.counter == 33
