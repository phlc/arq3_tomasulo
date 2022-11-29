
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
            self.registers[name] = False
        self.registers["r0"] = 0


        #Reservation Stations
        self.reservation = {}
        for name in rs_names:
            self.reservation[name] = {}
            for field in rs_fields:
                self.reservation[name][field] = False

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

        
        #send instruction to reservation stations and reorder buffer
        if(len(new_state.instruction_queue["queue"])>0):
            inst = new_state.instruction_queue["queue"][0]["inst"]
            inst_parced = inst.replace(",", " ").split()
            addr = new_state.instruction_queue["queue"][0]["addr"]

            if(inst_parced[0] == "add" or inst_parced[0] == "addi" or inst_parced[0] == "sub"):

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

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "add1"
                    })

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

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "add2"
                    })

                   

            elif(inst_parced[0] == "beq"):
                if new_state.reservation["branch"]["busy"] != 1:
                    new_state.reservation["branch"]["busy"] = 1
                    new_state.instruction_queue["queue"].pop(0)
                

            elif(inst_parced[0] == "mul" or inst_parced[0] == "div"):
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

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "mult1"
                    })

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

                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "mult2"
                    })
                

            elif(inst_parced[0] == "lw"):
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
                    except:
                        new_state.reservation["load1"]["a"] = f'{imm} + ({source})'                    
                    
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "load1"
                    })


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
                    except:
                        new_state.reservation["load2"]["a"] = f'{imm} + ({source})'                    
                    
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": inst_parced[1],
                        "value": "load2"
                    })

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
                        new_state.reservation["store"]["a"] = f'{imm} + ({source})'

                    try:
                        new_state.reservation["store"]["vj"] = int(value)
                        new_state.reservation["add2"]["qj"] = " "
                    except:
                        new_state.reservation["add2"]["qj"] = value
                        new_state.reservation["add2"]["vj"] = " "                  
                    
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": new_state.reservation["store"]["a"],
                        "value": value
                    })

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

        