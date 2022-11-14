
# Global Variables

global clock, pc, inst_cache, data_cache
clock = 0
pc = 0


def load(instructions, data):
    global inst_cache
    global data_cache
    inst_cache =  instructions
    data_cache = data


def run():
    global clock
    global pc
    clock+=1
    pc+=4
