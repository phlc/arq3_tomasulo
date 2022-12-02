global rs_names, rs_fields, rg_names

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