
class State:
    def __init__(self):
        #control
        self.clock = 0
        self.pc = 0

        #instruction cache
        self.instruction_cache = {
            "cache": [],
            "size": 0
        }

        #data cache
        self.data_cache = {
            "cache": [],
            "size": 0
        }

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
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_mult1 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_mult2 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add1 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add2 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_add3 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_load1 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }
        self.reservation_load2 = {
            "addr": True,
            "busy": True,
            "op": True,
            "vj": True,
            "vk": True,
            "qj": True,
            "qk": True,
            "a": True
        }

        

# Global Variables

global states, actual_state
actual_state = None
states = []


def load(fname, inst_cache_size, data_cache_size, queue_size, reorder_buffer_size):
    global states, actual_state
    states = []
    tmp_inst_cache = []
    tmp_data_cache = []

    # Read file
    with open(fname, "r") as file:
        line = file.readline().strip('\n').strip().lower()
        while(line != ".data"):
            if(line != ""):
                tmp_inst_cache.append(line)
            line = file.readline().strip('\n').strip().lower()

        line = file.readline().strip('\n').strip().lower()
        while(line):
            if(line != ""):
                tmp_data_cache.append(line)
            line = file.readline().strip('\n').strip().lower()

    # Create First State
    tmp_state = State()

    #instruction cache
    i = 0
    while(i < inst_cache_size and i < len(tmp_inst_cache)):
        tmp_state.instruction_cache["cache"].append(tmp_inst_cache[i])
        i+=1
    tmp_state.instruction_cache["size"] = inst_cache_size

    #data cache
    i = 0
    while(i < data_cache_size and i < len(tmp_data_cache)):
        tmp_state.data_cache["cache"].append(tmp_data_cache[i])
        i+=1
    tmp_state.data_cache["size"] = data_cache_size

    #instruction queue
    tmp_state.instruction_queue["size"] = queue_size

    #reorder buffer
    tmp_state.reorder_buffer["size"] = reorder_buffer_size

    states.append(tmp_state)
    actual_state = states[0]


def run():
    pass
