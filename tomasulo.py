from state import State

# Global Variables

global _states, actual_state, state_count, rs_names, rs_fields, rg_names
global value_add1, value_add2, value_mult1, value_mult2
global value_branch, value_store, dest_store, value_load1, value_load2

actual_state = None
ecall_fetched = False
ecall_commited_at = 1000000
state_count = 0
_states = []
value_add1 = value_add2 = value_mult1 = value_mult2 = "-"
value_branch = value_store = dest_store = value_load1 = value_load2 = "-"

def load(fname, inst_cache_size, data_cache_size, queue_size, reorder_buffer_size):
    global _states, actual_state, state_count
    state_count = 0
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


def run(sign):
    global _states, actual_state, state_count, ecall_fetched, ecall_commited_at
    global value_add1, value_add2, value_mult1, value_mult2
    global value_branch, value_store, dest_store, value_load1, value_load2

    if(sign == "+"):
        if(state_count < ecall_commited_at):
            state_count += 1
    elif(sign == "-"):
        if(state_count > 0):
            state_count -= 1

    #state already exists
    if (state_count < len(_states)):
        actual_state = _states[state_count]

    #create new state
    else:
        #create new clone state
        new_state = actual_state.clone()

        #update clock
        new_state.clock += 1

        # check and commit reorder buffer
        if(len(new_state.reorder_buffer["buffer"])>0):
            next = new_state.reorder_buffer["buffer"][0]

            if(next["type"] == "ecall"):
                ecall_commited_at = state_count
                new_state.reorder_buffer["buffer"].pop(0)

            elif(next["type"] == "beq"):
                if(isinstance(next["value"], int)):
                    new_state.reorder_buffer["buffer"].pop(0)

            elif(next["type"] == "sw"):
                if(isinstance(next["value"], int) and isinstance(next["dest"], int)):
                    new_state.data_cache["cache"][next["dest"]] = next["value"]
                    new_state.reorder_buffer["buffer"].pop(0)
            else:
                if(isinstance(next["value"], int)):
                    new_state.registers[next["dest"]] = next["value"]
                    new_state.reorder_buffer["buffer"].pop(0)


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
        if (isinstance(new_state.reservation["store"]["vj"], int) and isinstance(new_state.reservation["store"]["vk"], int)):
            imm = int(new_state.reservation["store"]["a"].split("(")[0])
            value_store = new_state.reservation["store"]["vj"]
            dest_store = imm + new_state.reservation["store"]["vk"]
            for field in rs_fields:
                new_state.reservation["store"][field] = "-"


        #forward values
        if(isinstance(value_add1, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "add1"):
                    item["value"] = value_add1
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "add1"):
                        new_state.reservation[name][field] = value_add1
            value_add1 = " "

            
        if(isinstance(value_add2, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "add2"):
                    item["value"] = value_add2
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "add2"):
                        new_state.reservation[name][field] = value_add2
            value_add2 = " "

        if(isinstance(value_branch, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "branch"):
                    item["value"] = value_branch

        if(isinstance(value_mult1, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "mult1"):
                    item["value"] = value_mult1
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "mult1"):
                        new_state.reservation[name][field] = value_mult1
            value_mult1 = " "

        if(isinstance(value_mult2, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "mult2"):
                    item["value"] = value_mult2
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "mult2"):
                        new_state.reservation[name][field] = value_mult2
            value_mult2 = " "

        if(isinstance(value_load1, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "load1"):
                    item["value"] = value_load1
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "load1"):
                        new_state.reservation[name][field] = value_load1
            value_load1 = " "

        if(isinstance(value_load2, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["value"] == "load2"):
                    item["value"] = value_load2
            for name in rs_names:
                for field in rs_fields:
                    if(new_state.reservation[name][field] == "load2"):
                        new_state.reservation[name][field] = value_load2
            value_load2 = " "

        if(isinstance(value_store, int) and isinstance(dest_store, int)):
            for item in new_state.reorder_buffer["buffer"]:
                if(item["dest"] == "store"):
                    item["value"] = value_store
                    item["dest"] = dest_store
        

        
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
                        new_state.reservation["load1"]["a"] = f'{imm}({source})'
                        new_state.reservation["load1"]["vj"] = source
                        new_state.reservation["load1"]["vk"] = imm
                        new_state.reservation["load1"]["qk"] = " "
                        new_state.reservation["load1"]["qj"] = " "
                    except:
                        new_state.reservation["load1"]["a"] = f'{imm}({source})'
                        new_state.reservation["load1"]["qj"] = source
                        new_state.reservation["load1"]["vk"] = imm  
                        new_state.reservation["load1"]["qk"] = " "
                        new_state.reservation["load1"]["qj"] = " "                  
                    
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
                        new_state.reservation["load2"]["a"] = f'{imm}({source})'
                        new_state.reservation["load2"]["vj"] = source
                        new_state.reservation["load2"]["vk"] = imm
                        new_state.reservation["load2"]["qk"] = " "
                        new_state.reservation["load2"]["qj"] = " "
                    except:
                        new_state.reservation["load2"]["a"] = f'{imm}({source})'
                        new_state.reservation["load2"]["qj"] = source
                        new_state.reservation["load2"]["vk"] = imm  
                        new_state.reservation["load2"]["qk"] = " "
                        new_state.reservation["load2"]["qj"] = " " 
                    
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
                        new_state.reservation["store"]["vk"] = dest
                        new_state.reservation["store"]["qk"] = " "
                    except:
                        new_state.reservation["store"]["qk"] = dest
                        new_state.reservation["store"]["vk"] = " "
                    try:
                        new_state.reservation["store"]["vj"] = int(value)
                        new_state.reservation["store"]["qj"] = " "
                    except:
                        new_state.reservation["store"]["qj"] = value
                        new_state.reservation["store"]["vj"] = " "                  
                    
                    new_state.reservation["store"]["a"] = f'{imm}({dest})'
                    new_state.instruction_queue["queue"].pop(0)

                    #reorder buffer
                    new_state.reorder_buffer["buffer"].append({
                        "addr": addr,
                        "type": inst_parced[0],
                        "dest": "store",
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
                new_state.instruction_queue["queue"].pop(0)


            
        
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

        