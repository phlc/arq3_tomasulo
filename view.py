# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from ui_form import Ui_View
import tomasulo as tm

# Constants
global queue_size
global reorder_buffer_size

# Global Variables
global loaded, inst_cache, inst_queue, registers, data_cache, reorder_buffer

# Config
loaded = False
queue_size = 6
reorder_buffer_size = 10

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_View()
        self.ui.setupUi(self)

        #Global Variable
        global queue_size
        global loaded, inst_cache, inst_queue, clock, pc

        #Font
        font = QtGui.QFont()
        font.setBold(True)

        #Instruction Cache
        inst_cache = self.ui.inst_cache
        inst_cache.setColumnWidth(0,43)
        inst_cache.setColumnWidth(1,102)
        inst_cache.verticalHeader().setVisible(False)
        inst_cache.horizontalHeader().setVisible(False)
        inst_cache.setRowCount(1)
        inst_cache.setItem(0,0, QTableWidgetItem("Addr"))
        inst_cache.setItem(0,1, QTableWidgetItem(" Instruction"))
        inst_cache.item(0,0).setTextAlignment(Qt.AlignTop)
        inst_cache.item(0,1).setTextAlignment(Qt.AlignTop)
        inst_cache.item(0,0).setFont(font)
        inst_cache.item(0,1).setFont(font)
        inst_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Instruction Queue
        inst_queue = self.ui.inst_queue
        inst_queue.setColumnWidth(0,43)
        inst_queue.setColumnWidth(1,102)
        inst_queue.verticalHeader().setVisible(False)
        inst_queue.horizontalHeader().setVisible(False)
        inst_queue.setRowCount(queue_size+1)
        inst_queue.setItem(0,0, QTableWidgetItem("Id"))
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

        #Data Cache
        data_cache = self.ui.data_cache
        data_cache.setColumnWidth(0,45)
        data_cache.setColumnWidth(1,50)
        data_cache.setRowCount(1)
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

        #Reorder Buffer
        reorder_buffer = self.ui.reorder_buffer
        reorder_buffer.setColumnWidth(0,60)
        reorder_buffer.setColumnWidth(1,60)
        reorder_buffer.setColumnWidth(2,60)
        reorder_buffer.setColumnWidth(3,60)
        reorder_buffer.setRowCount(reorder_buffer_size + 1)
        reorder_buffer.verticalHeader().setVisible(False)
        reorder_buffer.horizontalHeader().setVisible(False)
        reorder_buffer.setItem(0,0, QTableWidgetItem("Id"))
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
        reservation.setItem(0,1, QTableWidgetItem("Id"))
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
        reservation.setItem(1,0, QTableWidgetItem("Branch"))
        reservation.setItem(2,0, QTableWidgetItem("Mult1"))
        reservation.setItem(3,0, QTableWidgetItem("Mult2"))
        reservation.setItem(4,0, QTableWidgetItem("Add1"))
        reservation.setItem(5,0, QTableWidgetItem("Add2"))
        reservation.setItem(6,0, QTableWidgetItem("Load1"))
        reservation.setItem(7,0, QTableWidgetItem("Load2"))
        reservation.setItem(8,0, QTableWidgetItem("Store"))
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
        global loaded
        fname = QFileDialog.getOpenFileName(self, "Load File", "", "Python Files (*.asm)")
        if fname:
            loaded = True
            fname = fname[0]
            tm.load(fname)


    def clock_plus(self):
        global loaded, queue_size, clock, pc
        if(not loaded):
            self.error()
        else:
            pass
            

    def clock_minus(self):
        global loaded, queue_size, clock, pc
        if(not loaded):
            self.error()
        else:
            pass

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
