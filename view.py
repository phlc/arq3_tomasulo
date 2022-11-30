# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from ui_form import Ui_View
import tomasulo as tm

# Constants
global inst_cache_size, data_cache_size, queue_size, reorder_buffer_size 
global rs_names, rs_fields, rg_names

# Global Control Variables
global loaded, state_count

# Global Gui Variables
global clock, pc, inst_cache, data_cache, inst_queue, registers, reorder_buffer

# Config
loaded = False
state_count = 0
inst_cache_size = 16
data_cache_size = 8
queue_size = 6
reorder_buffer_size = 10
rs_names = ["store", "branch", "mult1", "mult2", "add1", "add2", "load1", "load2"]
rs_fields = ["addr", "busy", "op", "vj", "vk", "qj", "qk", "a"]
rg_names = ["r0", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9"]
tm.rs_names = rs_names
tm.rs_fields = rs_fields
tm.rg_names = rg_names


class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_View()
        self.ui.setupUi(self)

        #global constants
        global inst_cache_size, data_cache_size, queue_size, reorder_buffer_size

        #global variables
        global loaded, state_count
        #globa gui variables
        global clock, pc, inst_cache, data_cache, inst_queue, reorder_buffer, registers, reservation

        #Font
        font = QtGui.QFont()
        font.setBold(True)

        #Control
        self.ui.control.setColumnWidth(0,50)
        self.ui.control.setColumnWidth(1,50)
        self.ui.control.verticalHeader().setVisible(False)
        self.ui.control.horizontalHeader().setVisible(False)
        self.ui.control.setItem(0,0, QTableWidgetItem("Clock"))
        self.ui.control.setItem(1,0, QTableWidgetItem("PC"))
        self.ui.control.item(0,0).setFont(font)
        self.ui.control.item(1,0).setFont(font)

        self.ui.control.setItem(0,1, QTableWidgetItem(""))
        self.ui.control.setItem(1,1, QTableWidgetItem(""))
        clock = self.ui.control.item(0,1)
        pc = self.ui.control.item(1,1)
        
        clock.setFont(font)
        pc.setFont(font)
        self.ui.control.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.control.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Instruction Cache
        inst_cache = self.ui.inst_cache
        inst_cache.setColumnWidth(0,43)
        inst_cache.setColumnWidth(1,102)
        inst_cache.verticalHeader().setVisible(False)
        inst_cache.horizontalHeader().setVisible(False)
        inst_cache.setRowCount(inst_cache_size+1)
        inst_cache.setItem(0,0, QTableWidgetItem("Addr"))
        inst_cache.setItem(0,1, QTableWidgetItem(" Instruction"))
        inst_cache.item(0,0).setTextAlignment(Qt.AlignTop)
        inst_cache.item(0,1).setTextAlignment(Qt.AlignTop)
        inst_cache.item(0,0).setFont(font)
        inst_cache.item(0,1).setFont(font)
        inst_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        inst_cache.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(1,inst_cache_size+1):
            inst_cache.setItem(i,0, QTableWidgetItem(""))
            inst_cache.setItem(i,1, QTableWidgetItem(""))

        #Data Cache
        data_cache = self.ui.data_cache
        data_cache.setColumnWidth(0,45)
        data_cache.setColumnWidth(1,50)
        data_cache.setRowCount(data_cache_size+1)
        data_cache.verticalHeader().setVisible(False)
        data_cache.horizontalHeader().setVisible(False)
        data_cache.setItem(0,0, QTableWidgetItem("Addr"))
        data_cache.setItem(0,1, QTableWidgetItem("Value"))
        data_cache.item(0,0).setTextAlignment(Qt.AlignLeft)
        data_cache.item(0,1).setTextAlignment(Qt.AlignLeft)
        data_cache.item(0,0).setFont(font)
        data_cache.item(0,1).setFont(font)
        data_cache.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        data_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(1,data_cache_size+1):
            data_cache.setItem(i,0, QTableWidgetItem(""))
            data_cache.setItem(i,1, QTableWidgetItem(""))

        #Instruction Queue
        inst_queue = self.ui.inst_queue
        inst_queue.setColumnWidth(0,43)
        inst_queue.setColumnWidth(1,102)
        inst_queue.verticalHeader().setVisible(False)
        inst_queue.horizontalHeader().setVisible(False)
        inst_queue.setRowCount(queue_size+1)
        inst_queue.setItem(0,0, QTableWidgetItem("Addr"))
        inst_queue.setItem(0,1, QTableWidgetItem(" Instruction"))
        inst_queue.item(0,0).setTextAlignment(Qt.AlignTop)
        inst_queue.item(0,1).setTextAlignment(Qt.AlignTop)
        inst_queue.item(0,0).setFont(font)
        inst_queue.item(0,1).setFont(font)
        inst_queue.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        inst_queue.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(1,queue_size+1):
            inst_queue.setItem(i,0, QTableWidgetItem(""))
            inst_queue.setItem(i,1, QTableWidgetItem(""))

        
        #Reorder Buffer
        reorder_buffer = self.ui.reorder_buffer
        reorder_buffer.setColumnWidth(0,60)
        reorder_buffer.setColumnWidth(1,60)
        reorder_buffer.setColumnWidth(2,60)
        reorder_buffer.setColumnWidth(3,60)
        reorder_buffer.setRowCount(reorder_buffer_size + 1)
        reorder_buffer.verticalHeader().setVisible(False)
        reorder_buffer.horizontalHeader().setVisible(False)
        reorder_buffer.setItem(0,0, QTableWidgetItem("Addr"))
        reorder_buffer.setItem(0,1, QTableWidgetItem("Type"))
        reorder_buffer.setItem(0,2, QTableWidgetItem("Dest"))
        reorder_buffer.setItem(0,3, QTableWidgetItem("Value"))
        reorder_buffer.item(0,0).setTextAlignment(Qt.AlignCenter)
        reorder_buffer.item(0,1).setTextAlignment(Qt.AlignCenter)
        reorder_buffer.item(0,2).setTextAlignment(Qt.AlignCenter)
        reorder_buffer.item(0,3).setTextAlignment(Qt.AlignCenter)
        reorder_buffer.item(0,0).setFont(font)
        reorder_buffer.item(0,1).setFont(font)
        reorder_buffer.item(0,2).setFont(font)
        reorder_buffer.item(0,3).setFont(font)
        reorder_buffer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        reorder_buffer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for row in range(1, reorder_buffer_size+1):    
            for col in range(0, 4):
                reorder_buffer.setItem(row,col, QTableWidgetItem(""))
                reorder_buffer.item(row,col).setTextAlignment(Qt.AlignCenter)
                

        #Registers
        registers = self.ui.registers
        registers.verticalHeader().setVisible(False)
        registers.horizontalHeader().setVisible(False)
        registers.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        registers.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(0, 10):
            registers.setItem(0,i, QTableWidgetItem(f'R{i}'))
            registers.setItem(1,i, QTableWidgetItem(""))
            registers.item(0,i).setTextAlignment(Qt.AlignCenter)
            registers.item(1,i).setTextAlignment(Qt.AlignCenter)


        # Reservation Stations
        reservation = self.ui.reservation
        reservation.setColumnWidth(0,60)
        reservation.setColumnWidth(1,60)
        reservation.setColumnWidth(2,60)
        reservation.setColumnWidth(3,60)
        reservation.setColumnWidth(4,60)
        reservation.setColumnWidth(5,60)
        reservation.setColumnWidth(6,60)
        reservation.setColumnWidth(7,60)
        reservation.setColumnWidth(8,60)
        reservation.setRowCount(9)
        reservation.verticalHeader().setVisible(False)
        reservation.horizontalHeader().setVisible(False)
        reservation.setItem(0,0, QTableWidgetItem("Name"))
        reservation.setItem(0,1, QTableWidgetItem("Addr"))
        reservation.setItem(0,2, QTableWidgetItem("Busy"))
        reservation.setItem(0,3, QTableWidgetItem("Op"))
        reservation.setItem(0,4, QTableWidgetItem("Vj"))
        reservation.setItem(0,5, QTableWidgetItem("Vk"))
        reservation.setItem(0,6, QTableWidgetItem("Qj"))
        reservation.setItem(0,7, QTableWidgetItem("Qk"))
        reservation.setItem(0,8, QTableWidgetItem("A"))
        for i in range(0,9):
            reservation.item(0,i).setFont(font)
            reservation.item(0,i).setTextAlignment(Qt.AlignCenter)

        i = 1
        for name in rs_names:
            reservation.setItem(i,0, QTableWidgetItem(name))
            i+=1

        for row in range(1, 9):    
            for col in range(1, 9):
                reservation.setItem(row,col, QTableWidgetItem(""))
                reservation.item(row,col).setTextAlignment(Qt.AlignCenter)
        
        reservation.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        reservation.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        # Menu Bar        
        self.ui.choose_file.triggered.connect(self.loadFile)

        # Clock Buttons
        self.ui.clock_btn_plus.clicked.connect(self.clock_plus)
        self.ui.clock_btn_minus.clicked.connect(self.clock_minus)

    
    def loadFile(self):
        global inst_cache_size, data_cache_size, queue_size, reorder_buffer_size

        global loaded, state_count
        fname = QFileDialog.getOpenFileName(self, "Load File", "", "Python Files (*.asm)")
        if fname:
            loaded = True
            state_count = 0
            fname = fname[0]
            tm.load(fname, inst_cache_size, data_cache_size, queue_size, reorder_buffer_size)
            self.show_data()
        else:
            self.error()

    def show_data(self):
        global clock, pc, inst_cache, data_cache, inst_queue, reorder_buffer, registers, reservation

        #control
        clock.setText(str(tm.actual_state.clock))
        pc.setText(str(tm.actual_state.pc))
        

        #instruction cache
        i = 0
        while(i < len(tm.actual_state.instruction_cache["cache"])):
            inst_cache.item(i+1,0).setText(str(i*4))
            inst_cache.item(i+1,1).setText(str(tm.actual_state.instruction_cache["cache"][i]))
            i+=1
        while(i < tm.actual_state.instruction_cache["size"]):
            inst_cache.item(i+1,0).setText(str(i*4))
            inst_cache.item(i+1,1).setText("-")
            i+=1

        for i in range(1, inst_cache_size):
            inst_cache.item(i, 0).setBackground(QtGui.QBrush(QtGui.QColor("transparent")))
        inst_cache.item(tm.actual_state.pc//4 + 1, 0).setBackground(QtGui.QBrush(QtGui.QColor("red")))

        #data cache
        i = 0
        while(i < len(tm.actual_state.data_cache["cache"])):
            data_cache.item(i+1,0).setText(str(i*4))
            data_cache.item(i+1,1).setText(str(tm.actual_state.data_cache["cache"][i]))
            i+=1
        while(i < tm.actual_state.data_cache["size"]):
            data_cache.item(i+1,0).setText(str(i*4))
            data_cache.item(i+1,1).setText("-")
            i+=1

        #instruction queue
        i = 0
        while(i < len(tm.actual_state.instruction_queue["queue"])):
            inst_queue.item(queue_size - i,0).setText(str(tm.actual_state.instruction_queue["queue"][i]["addr"]))
            inst_queue.item(queue_size - i,1).setText(tm.actual_state.instruction_queue["queue"][i]["inst"])
            i+=1
        while(i < tm.actual_state.instruction_queue["size"]):
            inst_queue.item(queue_size - i,0).setText("-")
            inst_queue.item(queue_size - i,1).setText("-")
            i+=1

        #reorder buffer
        i = 0
        while(i < len(tm.actual_state.reorder_buffer["buffer"])):
            reorder_buffer.item(reorder_buffer_size - i,0).setText(str(tm.actual_state.reorder_buffer["buffer"][i]["addr"]))
            reorder_buffer.item(reorder_buffer_size - i,1).setText(str(tm.actual_state.reorder_buffer["buffer"][i]["type"]))
            reorder_buffer.item(reorder_buffer_size - i,2).setText(str(tm.actual_state.reorder_buffer["buffer"][i]["dest"]))
            reorder_buffer.item(reorder_buffer_size - i,3).setText(str(tm.actual_state.reorder_buffer["buffer"][i]["value"]))
            i+=1
        while(i < tm.actual_state.reorder_buffer["size"]):
            reorder_buffer.item(reorder_buffer_size - i,0).setText("-")
            reorder_buffer.item(reorder_buffer_size - i,1).setText("-")
            reorder_buffer.item(reorder_buffer_size - i,2).setText("-")
            reorder_buffer.item(reorder_buffer_size - i,3).setText("-")
            i+=1


        #registers
        for i, name in zip(range(0, 10), rg_names):    
            registers.item(1,i).setText(str(tm.actual_state.registers[name]))

        #reservation stations
        for i, name in zip(range(1, 9), rs_names):
            for j, field in zip(range(1, 9), rs_fields):
                reservation.item(i,j).setText(str(tm.actual_state.reservation[name][field]))
            

    def clock_plus(self):
        global loaded, state_count
        if(not loaded):
            self.error()
        else:
            state_count += 1
            tm.run(state_count)
            self.show_data()
            

    def clock_minus(self):
        global loaded, state_count
        if(not loaded):
            self.error()
        else:
            if(state_count > 0):
                state_count -= 1
            tm.run(state_count)
            self.show_data()

    def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("File not Loaded")
        msg.setInformativeText('Please load a valid .asm file')
        msg.setWindowTitle("File not Loaded")
        msg.exec_()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = View()
    widget.show()
    sys.exit(app.exec())
