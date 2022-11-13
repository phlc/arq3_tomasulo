# This Python file uses the following encoding: utf-8
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem
from PyQt5.QtCore import Qt

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_View

class View(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_View()
        self.ui.setupUi(self)

        #Font
        font = QtGui.QFont()
        font.setBold(True)

        #Instruction Cache
        self.ui.inst_cache.setColumnWidth(0,43)
        self.ui.inst_cache.setColumnWidth(1,102)
        self.ui.inst_cache.verticalHeader().setVisible(False)
        self.ui.inst_cache.horizontalHeader().setVisible(False)
        self.ui.inst_cache.setRowCount(1)
        self.ui.inst_cache.setItem(0,0, QTableWidgetItem("Addr"))
        self.ui.inst_cache.setItem(0,1, QTableWidgetItem("Instruction"))
        self.ui.inst_cache.item(0,0).setTextAlignment(Qt.AlignTop)
        self.ui.inst_cache.item(0,1).setTextAlignment(Qt.AlignTop)
        self.ui.inst_cache.item(0,0).setFont(font)
        self.ui.inst_cache.item(0,1).setFont(font)
        self.ui.inst_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Instruction Queue
        self.ui.inst_queue.setColumnWidth(0,43)
        self.ui.inst_queue.setColumnWidth(1,102)
        self.ui.inst_queue.verticalHeader().setVisible(False)
        self.ui.inst_queue.horizontalHeader().setVisible(False)
        self.ui.inst_queue.setRowCount(1)
        self.ui.inst_queue.setItem(0,0, QTableWidgetItem("Id"))
        self.ui.inst_queue.setItem(0,1, QTableWidgetItem("Instruction"))
        self.ui.inst_queue.item(0,0).setTextAlignment(Qt.AlignTop)
        self.ui.inst_queue.item(0,1).setTextAlignment(Qt.AlignTop)
        self.ui.inst_queue.item(0,0).setFont(font)
        self.ui.inst_queue.item(0,1).setFont(font)
        self.ui.inst_queue.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Control
        self.ui.control.setColumnWidth(0,50)
        self.ui.control.setColumnWidth(1,50)
        self.ui.control.verticalHeader().setVisible(False)
        self.ui.control.horizontalHeader().setVisible(False)
        self.ui.control.setItem(0,0, QTableWidgetItem("Clock"))
        self.ui.control.setItem(1,0, QTableWidgetItem("PC"))
        self.ui.control.item(0,0).setTextAlignment(Qt.AlignLeft)
        self.ui.control.item(1,0).setTextAlignment(Qt.AlignLeft)
        self.ui.control.item(0,0).setFont(font)
        self.ui.control.item(1,0).setFont(font)
        self.ui.control.setItem(0,1, QTableWidgetItem("0"))
        self.ui.control.setItem(1,1, QTableWidgetItem("0"))
        self.ui.control.item(0,1).setTextAlignment(Qt.AlignRight)
        self.ui.control.item(1,1).setTextAlignment(Qt.AlignRight)
        self.ui.control.item(0,1).setFont(font)
        self.ui.control.item(1,1).setFont(font)
        self.ui.control.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.control.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Registers
        self.ui.registers.verticalHeader().setVisible(False)
        self.ui.registers.horizontalHeader().setVisible(False)
        self.ui.registers.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.registers.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        for i in range(0, 10):
            self.ui.registers.setItem(0,i, QTableWidgetItem(f'R{i}'))
            self.ui.registers.setItem(1,i, QTableWidgetItem(str(0)))
            self.ui.registers.item(0,i).setTextAlignment(Qt.AlignCenter)
            self.ui.registers.item(1,i).setTextAlignment(Qt.AlignCenter)

        #Data Cache
        self.ui.data_cache.setColumnWidth(0,45)
        self.ui.data_cache.setColumnWidth(1,50)
        self.ui.data_cache.setRowCount(1)
        self.ui.data_cache.verticalHeader().setVisible(False)
        self.ui.data_cache.horizontalHeader().setVisible(False)
        self.ui.data_cache.setItem(0,0, QTableWidgetItem("Addr"))
        self.ui.data_cache.setItem(0,1, QTableWidgetItem("Value"))
        self.ui.data_cache.item(0,0).setTextAlignment(Qt.AlignLeft)
        self.ui.data_cache.item(0,1).setTextAlignment(Qt.AlignLeft)
        self.ui.data_cache.item(0,0).setFont(font)
        self.ui.data_cache.item(0,1).setFont(font)
        self.ui.data_cache.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.data_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        #Reorder Buffer
        self.ui.reorder_buffer.setColumnWidth(0,60)
        self.ui.reorder_buffer.setColumnWidth(1,60)
        self.ui.reorder_buffer.setColumnWidth(2,60)
        self.ui.reorder_buffer.setColumnWidth(3,60)
        self.ui.reorder_buffer.setRowCount(1)
        self.ui.reorder_buffer.verticalHeader().setVisible(False)
        self.ui.reorder_buffer.horizontalHeader().setVisible(False)
        self.ui.reorder_buffer.setItem(0,0, QTableWidgetItem("Id"))
        self.ui.reorder_buffer.setItem(0,1, QTableWidgetItem("Type"))
        self.ui.reorder_buffer.setItem(0,2, QTableWidgetItem("Dest"))
        self.ui.reorder_buffer.setItem(0,3, QTableWidgetItem("Value"))
        self.ui.reorder_buffer.item(0,0).setTextAlignment(Qt.AlignLeft)
        self.ui.reorder_buffer.item(0,1).setTextAlignment(Qt.AlignLeft)
        self.ui.reorder_buffer.item(0,2).setTextAlignment(Qt.AlignLeft)
        self.ui.reorder_buffer.item(0,3).setTextAlignment(Qt.AlignLeft)
        self.ui.reorder_buffer.item(0,0).setFont(font)
        self.ui.reorder_buffer.item(0,1).setFont(font)
        self.ui.reorder_buffer.item(0,2).setFont(font)
        self.ui.reorder_buffer.item(0,3).setFont(font)
        self.ui.reorder_buffer.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.reorder_buffer.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Reservation Stations
        self.ui.reservation.setColumnWidth(0,60)
        self.ui.reservation.setColumnWidth(1,60)
        self.ui.reservation.setColumnWidth(2,60)
        self.ui.reservation.setColumnWidth(3,60)
        self.ui.reservation.setColumnWidth(4,60)
        self.ui.reservation.setColumnWidth(5,60)
        self.ui.reservation.setColumnWidth(6,60)
        self.ui.reservation.setColumnWidth(7,60)
        self.ui.reservation.setColumnWidth(8,60)
        self.ui.reservation.setRowCount(9)
        self.ui.reservation.verticalHeader().setVisible(False)
        self.ui.reservation.horizontalHeader().setVisible(False)
        self.ui.reservation.setItem(0,0, QTableWidgetItem("Name"))
        self.ui.reservation.setItem(0,1, QTableWidgetItem("Id"))
        self.ui.reservation.setItem(0,2, QTableWidgetItem("Busy"))
        self.ui.reservation.setItem(0,3, QTableWidgetItem("Op"))
        self.ui.reservation.setItem(0,4, QTableWidgetItem("Vj"))
        self.ui.reservation.setItem(0,5, QTableWidgetItem("Vk"))
        self.ui.reservation.setItem(0,6, QTableWidgetItem("Qj"))
        self.ui.reservation.setItem(0,7, QTableWidgetItem("Qk"))
        self.ui.reservation.setItem(0,8, QTableWidgetItem("A"))
        for i in range(0,9):
            self.ui.reservation.item(0,i).setFont(font)
            self.ui.reservation.item(0,i).setTextAlignment(Qt.AlignCenter)
        self.ui.reservation.setItem(1,0, QTableWidgetItem("Branch"))
        self.ui.reservation.setItem(2,0, QTableWidgetItem("Mult1"))
        self.ui.reservation.setItem(3,0, QTableWidgetItem("Mult2"))
        self.ui.reservation.setItem(4,0, QTableWidgetItem("Add1"))
        self.ui.reservation.setItem(5,0, QTableWidgetItem("Add2"))
        self.ui.reservation.setItem(6,0, QTableWidgetItem("Add3"))
        self.ui.reservation.setItem(7,0, QTableWidgetItem("Load1"))
        self.ui.reservation.setItem(8,0, QTableWidgetItem("Load2"))
        
        self.ui.reservation.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ui.reservation.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        # Menu Bar        
        self.ui.choose_file.triggered.connect(self.loadFile)

    
    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, "Load File", "", "Python Files (*.asm)")
        if fname:
            fname = fname[0]
            file = open (fname, "r")
            instructions = []
            for line in file:
                instructions.append(line.strip("\n").strip(";").lower())
            
            addr = 0
            for i in range(0,len(instructions)):
                self.ui.inst_cache.insertRow(i+1)
                self.ui.inst_cache.setItem(i+1,0, QTableWidgetItem(str(addr)))
                self.ui.inst_cache.setItem(i+1,1, QTableWidgetItem(instructions[i]))
                addr+=4

            self.ui.inst_cache.item(1,0).setBackground(QtGui.QBrush(QtGui.QColor(255, 0, 0)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = View()
    widget.show()
    sys.exit(app.exec())
