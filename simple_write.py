from memory_engine import *
import sys

previous_values = {}

def print_on_change(variable_name, current_value, previous_values=previous_values):
    if variable_name not in previous_values or previous_values[variable_name] != current_value:
        print(f"{variable_name}: {current_value}")
        previous_values[variable_name] = current_value



arg = sys.argv[1]
game_mode = DolphinWord(0x804e66b8)
unk = DolphinWord(0x804e66ec)
somefunc = DolphinWord(0x8041f3f4)
game_mode_visual = DolphinWord(0x804e66bc)
unk2 = DolphinByte(0x804e66c0)
while True:
    print('Before:', somefunc.read())
    somefunc.write(int(arg))
    print('After:', somefunc.read())
    break