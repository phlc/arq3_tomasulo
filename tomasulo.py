
# Global Variables

global clock, pc, inst_cache, data_cache
clock = 0
pc = 0


def load(fname):
    global inst_cache
    global data_cache
    with open(fname, "r") as file:
        line = file.readline().strip('\n').strip().lower()
        while(line != ".data"):
            if(line != ""):
                inst_cache.append(line)
            line = file.readline().strip('\n').strip().lower()

        line = file.readline().strip('\n').strip().lower()
        while(line):
            if(line != ""):
                data_cache.append(line)
            line = file.readline().strip('\n').strip().lower()


def run():
    global clock
    global pc
    clock+=1
    pc+=4
