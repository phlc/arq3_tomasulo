
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
            self.registers[name] = "-"
        self.registers["r0"] = 0


        #Reservation Stations
        self.reservation = {}
        for name in rs_names:
            self.reservation[name] = {}
            for field in rs_fields:
                self.reservation[name][field] = "-"

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
        for item in self.instruction_queue["queue"]:
            cp.instruction_queue["queue"].append(
                {"addr": item["addr"],
                "inst": item["inst"]}
            )

        #reorder buffer
        cp.reorder_buffer["size"]  = self.reorder_buffer["size"]
        for item in self.reorder_buffer["buffer"]:
            cp.reorder_buffer["buffer"].append(
                {"addr": item["addr"],
                "type": item["type"],
                "dest": item["dest"],
                "value": item["value"]}
            )
          

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
global value_add1, value_add2, value_mult1, value_mult2
global value_branch, value_store, dest_store, value_load1, value_load2

actual_state = None
ecall_fetched = False
ecall_commited = False
_states = []
value_add1 = value_add2 = value_mult1 = value_mult2 = "-"
value_branch = value_store = dest_store = value_load1 = value_load2 = "-"

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
    global value_add1, value_add2, value_mult1, value_mult2
    global value_branch, value_store, dest_store, value_load1, value_load2

    #state already exists
    if (state_count < len(_states)):
        actual_state = _states[state_count]

    #create new state
    else:
        #create new clone state
        new_state = actual_state.clone()

        #update clock
        new_state.clock += 1



        #check reservation stations for ready instructions
        # add1
        if (isinstance(new_state.reservation["add1"]["vj"], int) and isinstance(new_state.reservation["add1"]["vk"], int)):
            if(new_state.reservation["add1"]["op"] == "sub"):
                value_add1 = new_state.reservation["add1"]["vj"] - new_state.reservation["add1"]["vk"]
            else:
                value_add1 = new_state.reservation["add1"]["vj"] + new_state.reservation["add1"]["vk"]
            for field in rs_fields:
                new_state.reservation["add1"][field] = "-"

        # add2
        if (isinstance(new_state.reservation["add2"]["vj"], int) and isinstance(new_state.reservation["add2"]["vk"], int)):
            if(new_state.reservation["add2"]["op"] == "sub"):
                value_add2 = new_state.reservation["add2"]["vj"] - new_state.reservation["add2"]["vk"]
            else:
                value_add2 = new_state.reservation["add2"]["vj"] + new_state.reservation["add2"]["vk"]
            for field in rs_fields:
                new_state.reservation["add2"][field] = "-"

        # branch
        if (isinstance(new_state.reservation["branch"]["vj"], int) and isinstance(new_state.reservation["branch"]["vk"], int)):
            value_branch = int(new_state.reservation["branch"]["vj"] == new_state.reservation["branch"]["vk"])
            for field in rs_fields:
                new_state.reservation["branch"][field] = "-"

        # mult1
        if (isinstance(new_state.reservation["mult1"]["vj"], int) and isinstance(new_state.reservation["mult1"]["vk"], int)):
            if(new_state.reservation["mult1"]["op"] == "mul"):
                value_mult1 = new_state.reservation["mult1"]["vj"] * new_state.reservation["mult1"]["vk"]
            else:
                value_mult1 = new_state.reservation["mult1"]["vj"] // new_state.reservation["mult1"]["vk"]
            for field in rs_fields:
                new_state.reservation["mult1"][field] = "-"

        # mult2
        if (isinstance(new_state.reservation["mult2"]["vj"], int) and isinstance(new_state.reservation["mult2"]["vk"], int)):
            if(new_state.reservation["mult2"]["op"] == "mul"):
                value_mult2 = new_state.reservation["mult2"]["vj"] * new_state.reservation["mult2"]["vk"]
            else:
                value_mult2 = new_state.reservation["mult2"]["vj"] // new_state.reservation["mult2"]["vk"]
            for field in rs_fields:
                new_state.reservation["mult2"][field] = "-"


        # load1
        if (isinstance(new_state.reservation["load1"]["vj"], int)):
            new_state.reservation["load1"]["a"] = new_state.reservation["load1"]["vj"] + new_state.reservation["load1"]["vk"]
            value_load1 = new_state.data_cache["cache"][new_state.reservation["load1"]["a"]//4]
            for field in rs_fields:
                new_state.reservation["load1"][field] = "-"

        # load2
        if (isinstance(new_state.reservation["load2"]["vj"], int)):
            new_state.reservation["load2"]["a"] = new_state.reservation["load2"]["vj"] + new_state.reservation["load2"]["vk"]
            value_load2 = new_state.data_cache["cache"][new_state.reservation["load2"]["a"]//4]
            for field in rs_fields:
                new_state.reservation["load2"][field] = "-"

        # store
        if (isinstance(new_state.reservation["store"]["a"], int) and isinstance(new_state.reservation["store"]["vj"], int)):
            dest_store = new_state.reservation["store"]["a"]
            value_store = new_state.reservation["store"]["vj"]
            for field in rs_fields:
                new_state.reservation["store"][field] = "-"


        #forward values
        if(isinstance(value_add1, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "add1"):
                    item["value"] = value_add1

            
        if(isinstance(value_add2, int)):
            pass
        if(isinstance(value_branch, int)):
            pass
        if(isinstance(value_mult1, int)):
            pass
        if(isinstance(value_mult2, int)):
            pass
        if(isinstance(value_load1, int)):
            pass
        if(isinstance(value_load2, int)):
            pass
        if(isinstance(value_store, int) and isinstance(dest_store, int)):
            pass
        

        
        #send instruction to reservation stations and reorder buffer
        if(len(new_state.instruction_queue["queue"])>0):
            inst = new_state.instruction_queue["queue"][0]["inst"]
            inst_parced = inst.replace(",", " ").split()
            addr = new_state.instruction_queue["queue"][0]["addr"]

            # adders
            if(inst_parced[0] == "add" or inst_parced[0] == "addi" or inst_parced[0] == "sub"):

                # add1
                if new_state.reservation["add1"]["busy"] != 1:
                    j = new_state.registers[inst_parced[2]]
                    k = ""
                    if(inst_parced[0] == "addi"):
                        k = inst_parced[3]
                    else:
                        k = new_state.registers[inst_parced[3]]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == inst_parced[2]:
                            j = item["value"]
                        if item["dest"] == inst_parced[3]:
                            k = item["value"]  

                    try:
                        new_state.reservation["add1"]["vj"] = int(j)
                        new_state.reservation["add1"]["qj"] = " "
                    except:
                        new_state.reservation["add1"]["qj"] = j
                        new_state.reservation["add1"]["vj"] = " "
                    try:
                        new_state.reservation["add1"]["vk"] = int(k)
                        new_state.reservation["add1"]["qk"] = " "
                    except:
                        new_state.reservation["add1"]["qk"] = k
                        new_state.reservation["add1"]["vk"] = " "

                    new_state.reservation["add1"]["addr"] = addr
                    new_state.reservation["add1"]["busy"] = 1
                    new_state.reservation["add1"]["op"] = inst_parced[0]
                    new_state.reservation["add1"]["a"] = " "

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "add1"
                    })

                # add2
                elif new_state.reservation["add2"]["busy"] != 1:
                    j = new_state.registers[inst_parced[2]]
                    k = ""
                    if(inst_parced[0] == "addi"):
                        k = inst_parced[3]
                    else:
                        k = new_state.registers[inst_parced[3]]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == inst_parced[2]:
                            j = item["value"]
                        if item["dest"] == inst_parced[3]:
                            k = item["value"]  

                    try:
                        new_state.reservation["add2"]["vj"] = int(j)
                        new_state.reservation["add2"]["qj"] = " "
                    except:
                        new_state.reservation["add2"]["qj"] = j
                        new_state.reservation["add2"]["vj"] = " "
                    try:
                        new_state.reservation["add2"]["vk"] = int(k)
                        new_state.reservation["add2"]["qk"] = " "
                    except:
                        new_state.reservation["add2"]["qk"] = k
                        new_state.reservation["add2"]["vk"] = " "

                    new_state.reservation["add2"]["addr"] = addr
                    new_state.reservation["add2"]["busy"] = 1
                    new_state.reservation["add2"]["op"] = inst_parced[0]
                    new_state.reservation["add2"]["a"] = " "

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "add2"
                    })

                   
            # branch
            elif(inst_parced[0] == "beq"):
                if new_state.reservation["branch"]["busy"] != 1:

                    j = new_state.registers[inst_parced[1]]
                    k = new_state.registers[inst_parced[2]]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == inst_parced[1]:
                            j = item["value"]
                        if item["dest"] == inst_parced[2]:
                            k = item["value"]

                    try:
                        new_state.reservation["branch"]["vj"] = int(j)
                        new_state.reservation["branch"]["qj"] = " "
                    except:
                        new_state.reservation["branch"]["qj"] = j
                        new_state.reservation["branch"]["vj"] = " "
                    try:
                        new_state.reservation["branch"]["vk"] = int(k)
                        new_state.reservation["branch"]["qk"] = " "
                    except:
                        new_state.reservation["branch"]["qk"] = k
                        new_state.reservation["branch"]["vk"] = " "

                    new_state.reservation["branch"]["addr"] = addr
                    new_state.reservation["branch"]["busy"] = 1
                    new_state.reservation["branch"]["op"] = inst_parced[0]
                    new_state.reservation["branch"]["a"] = int(addr) + int(inst_parced[3])

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": new_state.reservation["branch"]["a"],
                        "value": "branch"
                    })
                
            # mults
            elif(inst_parced[0] == "mul" or inst_parced[0] == "div"):

                # mult1
                if new_state.reservation["mult1"]["busy"] != 1:
                    j = new_state.registers[inst_parced[2]]
                    k = new_state.registers[inst_parced[3]]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == inst_parced[2]:
                            j = item["value"]
                        if item["dest"] == inst_parced[3]:
                            k = item["value"]  

                    try:
                        new_state.reservation["mult1"]["vj"] = int(j)
                        new_state.reservation["mult1"]["qj"] = " "
                    except:
                        new_state.reservation["mult1"]["qj"] = j
                        new_state.reservation["mult1"]["vj"] = " "
                    try:
                        new_state.reservation["mult1"]["vk"] = int(k)
                        new_state.reservation["mult1"]["qk"] = " "
                    except:
                        new_state.reservation["mult1"]["qk"] = k
                        new_state.reservation["mult1"]["vk"] = " "

                    new_state.reservation["mult1"]["addr"] = addr
                    new_state.reservation["mult1"]["busy"] = 1
                    new_state.reservation["mult1"]["op"] = inst_parced[0]
                    new_state.reservation["mult1"]["a"] = " "

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "mult1"
                    })

                # mult2
                elif new_state.reservation["mult2"]["busy"] != 1:
                    j = new_state.registers[inst_parced[2]]
                    k = new_state.registers[inst_parced[3]]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == inst_parced[2]:
                            j = item["value"]
                        if item["dest"] == inst_parced[3]:
                            k = item["value"]  

                    try:
                        new_state.reservation["mult2"]["vj"] = int(j)
                        new_state.reservation["mult2"]["qj"] = " "
                    except:
                        new_state.reservation["mult2"]["qj"] = j
                        new_state.reservation["mult2"]["vj"] = " "
                    try:
                        new_state.reservation["mult2"]["vk"] = int(k)
                        new_state.reservation["mult2"]["qk"] = " "
                    except:
                        new_state.reservation["mult2"]["qk"] = k
                        new_state.reservation["mult2"]["vk"] = " "

                    new_state.reservation["mult2"]["addr"] = addr
                    new_state.reservation["mult2"]["busy"] = 1
                    new_state.reservation["mult2"]["op"] = inst_parced[0]
                    new_state.reservation["mult2"]["a"] = " "

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "mult2"
                    })
                
            # loads
            elif(inst_parced[0] == "lw"):

                # load1
                if new_state.reservation["load1"]["busy"] != 1:
                    new_state.reservation["load1"]["addr"] = addr
                    new_state.reservation["load1"]["busy"] = 1
                    new_state.reservation["load1"]["op"] = inst_parced[0]
                    (imm, reg) = inst_parced[2].strip(")").split("(")
                    imm = int(imm)
                    source = new_state.registers[reg]
                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == reg:
                            source = item["value"]

                    try:
                        source = int(source)
                        new_state.reservation["load1"]["a"] = imm + source
                        new_state.reservation["load1"]["qj"] = " "
                        new_state.reservation["load1"]["vk"] = " "
                    except:
                        new_state.reservation["load1"]["a"] = f'{imm}+{source}'
                        new_state.reservation["load1"]["qj"] = source
                        new_state.reservation["load1"]["vk"] = imm                    
                    
        
                    new_state.reservation["load1"]["qk"] = " "
                    new_state.reservation["load1"]["vj"] = " "
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "load1"
                    })

                # load2
                elif new_state.reservation["load2"]["busy"] != 1:
                    new_state.reservation["load2"]["addr"] = addr
                    new_state.reservation["load2"]["busy"] = 1
                    new_state.reservation["load2"]["op"] = inst_parced[0]
                    (imm, reg) = inst_parced[2].strip(")").split("(")
                    imm = int(imm)
                    source = new_state.registers[reg]
                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == reg:
                            source = item["value"]

                    try:
                        source = int(source)
                        new_state.reservation["load2"]["a"] = imm + source
                        new_state.reservation["load2"]["qj"] = " "
                        new_state.reservation["load2"]["vk"] = " "
                    except:
                        new_state.reservation["load2"]["a"] = f'{imm}+{source}'
                        new_state.reservation["load2"]["qj"] = source
                        new_state.reservation["load2"]["vk"] = imm                    
                    
        
                    new_state.reservation["load2"]["qk"] = " "
                    new_state.reservation["load2"]["vj"] = " "
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "load2"
                    })

            # store
            elif(inst_parced[0] == "sw"):
                if new_state.reservation["store"]["busy"] != 1:
                    new_state.reservation["store"]["addr"] = addr
                    new_state.reservation["store"]["busy"] = 1
                    new_state.reservation["store"]["op"] = inst_parced[0]
                    (imm, reg) = inst_parced[2].strip(")").split("(")
                    imm = int(imm)
                    value = new_state.registers[inst_parced[1]]
                    dest = new_state.registers[reg]

                    for item in new_state.reorder_buffer["buffer"]:
                        if item["dest"] == reg:
                            dest = item["value"]
                        if item["dest"] == inst_parced[1]:
                            value = item["value"]

                    try:
                        dest = int(dest)
                        new_state.reservation["store"]["a"] = imm + dest
                    except:
                        new_state.reservation["store"]["a"] = f'{imm}+{source}'

                    try:
                        new_state.reservation["store"]["vj"] = int(value)
                        new_state.reservation["store"]["qj"] = " "
                    except:
                        new_state.reservation["store"]["qj"] = value
                        new_state.reservation["store"]["vj"] = " "                  
                    
                    new_state.reservation["store"]["qk"] = " "
                    new_state.reservation["store"]["vk"] = " "
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": new_state.reservation["store"]["a"],
                        "value": value
                    })

            # ecall
            elif(inst_parced[0] == "ecall"):
                #reorder buffer
                new_state.reorder_buffer["buffer"].append({
                    "addr": addr,
                    "type": inst_parced[0],
                    "dest": " ",
                    "value": " "
                })

            
        
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

        