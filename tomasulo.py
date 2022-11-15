
class State:
    def __init__(self):
        #control
        self.clock = 0
        self.pc = 0

        #instruction cache
        self.instruction_cache = []

        #data cache
        self.data_cache = []

        #instruction queue
        self.instruction_queue = {
            "queue": [],
            "size": 0
        }

        #reorder buffer
        self.reorder_buffer = {
            "buffer": [],
            "size": 0
        }

        #registers
        self.registers = {
            "r0": True,
            "r1": True,
            "r2": True,
            "r3": True,
            "r4": True,
            "r5": True,
            "r6": True,
            "r7": True,
            "r8": True,
            "r9": True,
        }


        #Reservation Stations
        self.reservation_branch = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_mult1 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_mult2 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add1 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add2 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add3 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_load1 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_load2 = {
            "id": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }

        

# Global Variables

global states
states = []


def load(fname):
    global estates
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
