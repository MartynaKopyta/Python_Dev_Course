# Useful built-in module - pdb - Python Debugger
import pdb

def add(a, b):
    # print(a + b)
    pdb.set_trace()
    return a + b

# Opens the debugger, help can show all the commands
print(add(4, 6))