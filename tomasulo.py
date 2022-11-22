
class State:
    def __init__(self):
        #global constants
        global rs_names, rs_fields, rg_names

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
        self.registers = {}
        for name in rg_names:
            self.registers[name] = True
        self.registers["r0"] = 0


        #Reservation Stations
        self.reservation = {}
        for name in rs_names:
            self.reservation[name] = {}
            for field in rs_fields:
                self.reservation[name][field] = True

    def clone(self):
        #global constants
        global rs_names, rs_fields, rg_names

        #create copy
        cp = State()
        
        #control
        cp.clock = self.clock
        cp.pc = self.pc

        #instruction cache
        cp.instruction_cache["size"] = self.instruction_cache["size"]
        for item in self.instruction_cache["cache"]:
            cp.instruction_cache["cache"].append(item)

        #data cache
        cp.data_cache["size"] = self.data_cache["size"]
        for item in self.data_cache["cache"]:
            cp.data_cache["cache"].append(item)

        #instruction queue
        cp.instruction_queue["size"] = self.instruction_queue["size"]
        i = 0
        for item in self.instruction_queue["queue"]:
            cp.instruction_queue["queue"].append(
                {"addr": item["addr"],
                "inst": item["inst"]}
            )
            i+=1

        #reorder buffer
        self.reorder_buffer = {
            "buffer": [],
            "size": 0
        }

        #reorder buffer
        cp.reorder_buffer["size"]  = self.reorder_buffer["size"]
        i = 0
        for item in self.reorder_buffer["buffer"]:
            cp.reorder_buffer["buffer"].append(
                {"addr": item["addr"],
                "type": item["type"],
                "dest": item["dest"],
                "value": item["value"]}
            )
            i+=1

        #registers
        for name in rg_names:
            cp.registers[name] = self.registers[name]

        #Reservation Stations
        for name in rs_names:
            cp.reservation[name] = {}
            for field in rs_fields:
                cp.reservation[name][field] = self.reservation[name][field]

        return cp



# Global Variables

global _states, actual_state, rs_names, rs_fields, rg_names
actual_state = None
ecall_fetched = False
ecall_commited = False
_states = []


def load(fname, inst_cache_size, data_cache_size, queue_size, reorder_buffer_size):
    global _states, actual_state
    actual_state = None
    _states = []
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
                tmp_data_cache.append(int(line))
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

    _states.append(tmp_state)
    actual_state = _states[0]


def run(state_count):
    global _states, actual_state, ecall_fetched, ecall_commited

    #state already exists
    if (state_count < len(_states)):
        actual_state = _states[state_count]

    #create new state
    else:
        #create new clone state
        new_state = actual_state.clone()

        #update clock
        new_state.clock += 1

        
        #send instruction to reservation stations
        if(len(new_state.instruction_queue["queue"])>0):
            inst = new_state.instruction_queue["queue"][0]["inst"]
            addr = new_state.instruction_queue["queue"][0]["addr"]
            inst_parced = inst.replace(",", " ").split()
            if(inst_parced[0] == "add"):
                pass
            elif(inst_parced[0] == "addi"):
                pass
            elif(inst_parced[0] == "sub"):
                pass
            elif(inst_parced[0] == "beq"):
                pass
            elif(inst_parced[0] == "mul"):
                pass
            elif(inst_parced[0] == "div"):
                pass
            elif(inst_parced[0] == "lw"):
                pass
            elif(inst_parced[0] == "sw"):
                pass
            elif(inst_parced[0] == "ecall"):
                pass
        
        #fetch instruction send to queue
        if(not ecall_fetched):
            addr = new_state.pc
            inst = new_state.instruction_cache["cache"][addr//4]
            new_state.instruction_queue["queue"].append({"addr": addr, "inst": inst})
            new_state.pc += 4
            if(inst == 'ecall'):
                ecall_fetched = True
                         


        #update actual_state and _states 
        _states.append(new_state)
        actual_state = _states[state_count]

        