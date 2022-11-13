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

        #Instruction Cache
        self.ui.inst_cache.setColumnWidth(0,43)
        self.ui.inst_cache.setColumnWidth(1,99)
        self.ui.inst_cache.verticalHeader().setVisible(False)
        self.ui.inst_cache.horizontalHeader().setVisible(False)
        self.ui.inst_cache.setRowCount(1)
        self.ui.inst_cache.setItem(0,0, QTableWidgetItem("Addr"))
        self.ui.inst_cache.setItem(0,1, QTableWidgetItem("Instruction"))
        font = QtGui.QFont()
        font.setBold(True)
        self.ui.inst_cache.item(0,0).setTextAlignment(Qt.AlignTop)
        self.ui.inst_cache.item(0,1).setTextAlignment(Qt.AlignTop)
        self.ui.inst_cache.item(0,0).setFont(font)
        self.ui.inst_cache.item(0,1).setFont(font)
        self.ui.inst_cache.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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




        self.ui.choose_file.triggered.connect(self.loadFile)

    
    def loadFile(self):
        fname = QFileDialog.getOpenFileName(self, "Load File", "", "Python Files (*.asm)")
        if fname:
            fname = fname[0]
            file = open (fname, "r")
            instructions = []
            for line in file:
                instructions.append(line.strip("\n").strip(";"))
            
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
