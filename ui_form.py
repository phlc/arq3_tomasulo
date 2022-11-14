# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(1200, 824)
        View.setMinimumSize(QtCore.QSize(1200, 800))
        View.setMaximumSize(QtCore.QSize(1200, 824))
        View.setStyleSheet("QWidget#centralwidget{\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(66, 66, 66, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}")
        self.centralwidget = QtWidgets.QWidget(View)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 800))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 800))
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(330, 20, 540, 42))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet("")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.clock_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clock_btn.setGeometry(QtCore.QRect(1070, 710, 120, 50))
        self.clock_btn.setStyleSheet("QPushButton#clock_btn{\n"
"border-radius:20;\n"
"background-color: rgb(94, 94, 94);\n"
"color:rgb(235, 235, 235);\n"
"font: 700 20pt \"Arial\";\n"
"}\n"
"QPushButton#clock_btn:pressed{\n"
"border-style:solid;\n"
"border-width:2px;\n"
"}")
        self.clock_btn.setObjectName("clock_btn")
        self.inst_cache = QtWidgets.QTableWidget(self.centralwidget)
        self.inst_cache.setGeometry(QtCore.QRect(30, 100, 151, 271))
        self.inst_cache.setObjectName("inst_cache")
        self.inst_cache.setColumnCount(2)
        self.inst_cache.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.inst_cache.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inst_cache.setHorizontalHeaderItem(1, item)
        self.inst_cache_t = QtWidgets.QLabel(self.centralwidget)
        self.inst_cache_t.setGeometry(QtCore.QRect(30, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.inst_cache_t.setFont(font)
        self.inst_cache_t.setStyleSheet("")
        self.inst_cache_t.setAlignment(QtCore.Qt.AlignCenter)
        self.inst_cache_t.setObjectName("inst_cache_t")
        self.control_t = QtWidgets.QLabel(self.centralwidget)
        self.control_t.setGeometry(QtCore.QRect(990, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.control_t.setFont(font)
        self.control_t.setStyleSheet("color: rgb(94, 94, 94)")
        self.control_t.setAlignment(QtCore.Qt.AlignCenter)
        self.control_t.setObjectName("control_t")
        self.control = QtWidgets.QTableWidget(self.centralwidget)
        self.control.setGeometry(QtCore.QRect(1000, 110, 121, 61))
        self.control.setObjectName("control")
        self.control.setColumnCount(2)
        self.control.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.control.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.control.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.control.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.control.setHorizontalHeaderItem(1, item)
        self.registers = QtWidgets.QTableWidget(self.centralwidget)
        self.registers.setGeometry(QtCore.QRect(30, 700, 1001, 61))
        self.registers.setObjectName("registers")
        self.registers.setColumnCount(10)
        self.registers.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.registers.setHorizontalHeaderItem(9, item)
        self.register_t = QtWidgets.QLabel(self.centralwidget)
        self.register_t.setGeometry(QtCore.QRect(30, 650, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.register_t.setFont(font)
        self.register_t.setStyleSheet("")
        self.register_t.setObjectName("register_t")
        self.reorder_buffer = QtWidgets.QTableWidget(self.centralwidget)
        self.reorder_buffer.setGeometry(QtCore.QRect(940, 290, 241, 341))
        self.reorder_buffer.setObjectName("reorder_buffer")
        self.reorder_buffer.setColumnCount(4)
        self.reorder_buffer.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.reorder_buffer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reorder_buffer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reorder_buffer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reorder_buffer.setHorizontalHeaderItem(3, item)
        self.reorder_buffer_t = QtWidgets.QLabel(self.centralwidget)
        self.reorder_buffer_t.setGeometry(QtCore.QRect(990, 260, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.reorder_buffer_t.setFont(font)
        self.reorder_buffer_t.setStyleSheet("color: rgb(94, 94, 94)")
        self.reorder_buffer_t.setAlignment(QtCore.Qt.AlignCenter)
        self.reorder_buffer_t.setObjectName("reorder_buffer_t")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(70, 680, 20, 21))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(170, 680, 20, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(270, 681, 20, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(370, 680, 20, 21))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(470, 680, 20, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(570, 679, 20, 21))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(770, 679, 20, 21))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(670, 680, 20, 20))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(970, 679, 20, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(870, 680, 20, 20))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(79, 670, 991, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(1060, 630, 20, 51))
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.adders = QtWidgets.QLabel(self.centralwidget)
        self.adders.setGeometry(QtCore.QRect(400, 590, 91, 31))
        self.adders.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.adders.setAlignment(QtCore.Qt.AlignCenter)
        self.adders.setObjectName("adders")
        self.mult = QtWidgets.QLabel(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(580, 590, 91, 31))
        self.mult.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.mult.setAlignment(QtCore.Qt.AlignCenter)
        self.mult.setObjectName("mult")
        self.branch = QtWidgets.QLabel(self.centralwidget)
        self.branch.setGeometry(QtCore.QRect(760, 590, 91, 31))
        self.branch.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.branch.setAlignment(QtCore.Qt.AlignCenter)
        self.branch.setObjectName("branch")
        self.reservation = QtWidgets.QTableWidget(self.centralwidget)
        self.reservation.setGeometry(QtCore.QRect(310, 200, 541, 271))
        self.reservation.setObjectName("reservation")
        self.reservation.setColumnCount(9)
        self.reservation.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.reservation.setHorizontalHeaderItem(8, item)
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(850, 450, 11, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(850, 416, 11, 31))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(850, 360, 21, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(850, 390, 21, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(850, 330, 21, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(850, 300, 31, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(850, 270, 31, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(850, 240, 41, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(850, 430, 21, 61))
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(860, 339, 21, 171))
        self.line_22.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(870, 279, 21, 251))
        self.line_23.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(880, 248, 21, 301))
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.data_cache = QtWidgets.QTableWidget(self.centralwidget)
        self.data_cache.setGeometry(QtCore.QRect(230, 510, 101, 161))
        self.data_cache.setObjectName("data_cache")
        self.data_cache.setColumnCount(2)
        self.data_cache.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.data_cache.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.data_cache.setHorizontalHeaderItem(1, item)
        self.data_cache_t = QtWidgets.QLabel(self.centralwidget)
        self.data_cache_t.setGeometry(QtCore.QRect(240, 480, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.data_cache_t.setFont(font)
        self.data_cache_t.setStyleSheet("")
        self.data_cache_t.setAlignment(QtCore.Qt.AlignCenter)
        self.data_cache_t.setObjectName("data_cache_t")
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(340, 480, 521, 20))
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setGeometry(QtCore.QRect(440, 500, 431, 20))
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralwidget)
        self.line_27.setGeometry(QtCore.QRect(620, 520, 261, 20))
        self.line_27.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralwidget)
        self.line_28.setGeometry(QtCore.QRect(800, 540, 91, 20))
        self.line_28.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_29 = QtWidgets.QFrame(self.centralwidget)
        self.line_29.setGeometry(QtCore.QRect(330, 489, 20, 30))
        self.line_29.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(430, 510, 20, 81))
        self.line_30.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.centralwidget)
        self.line_31.setGeometry(QtCore.QRect(610, 530, 20, 61))
        self.line_31.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.line_32 = QtWidgets.QFrame(self.centralwidget)
        self.line_32.setGeometry(QtCore.QRect(790, 550, 20, 41))
        self.line_32.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_32.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_32.setObjectName("line_32")
        self.line_33 = QtWidgets.QFrame(self.centralwidget)
        self.line_33.setGeometry(QtCore.QRect(331, 640, 581, 20))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.line_34 = QtWidgets.QFrame(self.centralwidget)
        self.line_34.setGeometry(QtCore.QRect(902, 268, 20, 411))
        self.line_34.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_34.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_34.setObjectName("line_34")
        self.line_35 = QtWidgets.QFrame(self.centralwidget)
        self.line_35.setGeometry(QtCore.QRect(911, 260, 70, 16))
        self.line_35.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_35.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_35.setObjectName("line_35")
        self.line_36 = QtWidgets.QFrame(self.centralwidget)
        self.line_36.setGeometry(QtCore.QRect(970, 268, 20, 23))
        self.line_36.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_36.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_36.setObjectName("line_36")
        self.line_37 = QtWidgets.QFrame(self.centralwidget)
        self.line_37.setGeometry(QtCore.QRect(430, 620, 16, 31))
        self.line_37.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_37.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_37.setObjectName("line_37")
        self.line_38 = QtWidgets.QFrame(self.centralwidget)
        self.line_38.setGeometry(QtCore.QRect(610, 620, 16, 31))
        self.line_38.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(self.centralwidget)
        self.line_39.setGeometry(QtCore.QRect(790, 620, 16, 31))
        self.line_39.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.inst_queue_t = QtWidgets.QLabel(self.centralwidget)
        self.inst_queue_t.setGeometry(QtCore.QRect(30, 390, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.inst_queue_t.setFont(font)
        self.inst_queue_t.setStyleSheet("")
        self.inst_queue_t.setAlignment(QtCore.Qt.AlignCenter)
        self.inst_queue_t.setObjectName("inst_queue_t")
        self.inst_queue = QtWidgets.QTableWidget(self.centralwidget)
        self.inst_queue.setGeometry(QtCore.QRect(30, 420, 151, 211))
        self.inst_queue.setObjectName("inst_queue")
        self.inst_queue.setColumnCount(2)
        self.inst_queue.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.inst_queue.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.inst_queue.setHorizontalHeaderItem(1, item)
        self.line_40 = QtWidgets.QFrame(self.centralwidget)
        self.line_40.setGeometry(QtCore.QRect(180, 600, 30, 20))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.line_41 = QtWidgets.QFrame(self.centralwidget)
        self.line_41.setGeometry(QtCore.QRect(180, 430, 21, 16))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.line_42 = QtWidgets.QFrame(self.centralwidget)
        self.line_42.setGeometry(QtCore.QRect(180, 330, 21, 16))
        self.line_42.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_42.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_42.setObjectName("line_42")
        self.line_43 = QtWidgets.QFrame(self.centralwidget)
        self.line_43.setGeometry(QtCore.QRect(190, 338, 20, 99))
        self.line_43.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_43.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_43.setObjectName("line_43")
        self.line_44 = QtWidgets.QFrame(self.centralwidget)
        self.line_44.setGeometry(QtCore.QRect(200, 227, 20, 382))
        self.line_44.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_44.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_44.setObjectName("line_44")
        self.line_45 = QtWidgets.QFrame(self.centralwidget)
        self.line_45.setGeometry(QtCore.QRect(210, 220, 101, 16))
        self.line_45.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_45.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_45.setObjectName("line_45")
        self.line_46 = QtWidgets.QFrame(self.centralwidget)
        self.line_46.setGeometry(QtCore.QRect(180, 140, 821, 20))
        self.line_46.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_46.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_46.setObjectName("line_46")
        self.line_47 = QtWidgets.QFrame(self.centralwidget)
        self.line_47.setGeometry(QtCore.QRect(330, 510, 11, 16))
        self.line_47.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_47.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_47.setObjectName("line_47")
        View.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(View)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menuBar.setObjectName("menuBar")
        self.load_file_2 = QtWidgets.QMenu(self.menuBar)
        self.load_file_2.setObjectName("load_file_2")
        View.setMenuBar(self.menuBar)
        self.choose_file = QtWidgets.QAction(View)
        self.choose_file.setObjectName("choose_file")
        self.load_file_2.addAction(self.choose_file)
        self.menuBar.addAction(self.load_file_2.menuAction())

        self.retranslateUi(View)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        _translate = QtCore.QCoreApplication.translate
        View.setWindowTitle(_translate("View", "View"))
        self.title.setText(_translate("View", "Tomasulo\'s Simulator"))
        self.clock_btn.setText(_translate("View", "Clock"))
        item = self.inst_cache.horizontalHeaderItem(0)
        item.setText(_translate("View", "Addr"))
        item = self.inst_cache.horizontalHeaderItem(1)
        item.setText(_translate("View", "Instruction"))
        self.inst_cache_t.setText(_translate("View", "Instruction Cache"))
        self.control_t.setText(_translate("View", "Control"))
        item = self.control.verticalHeaderItem(0)
        item.setText(_translate("View", "Clock"))
        item = self.control.verticalHeaderItem(1)
        item.setText(_translate("View", "PC"))
        item = self.control.horizontalHeaderItem(0)
        item.setText(_translate("View", "New Column"))
        item = self.control.horizontalHeaderItem(1)
        item.setText(_translate("View", "Value"))
        item = self.registers.verticalHeaderItem(0)
        item.setText(_translate("View", "New Row"))
        item = self.registers.verticalHeaderItem(1)
        item.setText(_translate("View", "Name"))
        item = self.registers.horizontalHeaderItem(0)
        item.setText(_translate("View", "R0"))
        item = self.registers.horizontalHeaderItem(1)
        item.setText(_translate("View", "R1"))
        item = self.registers.horizontalHeaderItem(2)
        item.setText(_translate("View", "R2"))
        item = self.registers.horizontalHeaderItem(3)
        item.setText(_translate("View", "R3"))
        item = self.registers.horizontalHeaderItem(4)
        item.setText(_translate("View", "R4"))
        item = self.registers.horizontalHeaderItem(5)
        item.setText(_translate("View", "R5"))
        item = self.registers.horizontalHeaderItem(6)
        item.setText(_translate("View", "R6"))
        item = self.registers.horizontalHeaderItem(7)
        item.setText(_translate("View", "R7"))
        item = self.registers.horizontalHeaderItem(8)
        item.setText(_translate("View", "R8"))
        item = self.registers.horizontalHeaderItem(9)
        item.setText(_translate("View", "R9"))
        self.register_t.setText(_translate("View", " Registers"))
        item = self.reorder_buffer.horizontalHeaderItem(0)
        item.setText(_translate("View", "Addr"))
        item = self.reorder_buffer.horizontalHeaderItem(1)
        item.setText(_translate("View", "Type"))
        item = self.reorder_buffer.horizontalHeaderItem(2)
        item.setText(_translate("View", "Destination"))
        item = self.reorder_buffer.horizontalHeaderItem(3)
        item.setText(_translate("View", "Result"))
        self.reorder_buffer_t.setText(_translate("View", "Reorder Buffer"))
        self.adders.setText(_translate("View", "Adders"))
        self.mult.setText(_translate("View", "Mult"))
        self.branch.setText(_translate("View", "Branch"))
        item = self.reservation.horizontalHeaderItem(0)
        item.setText(_translate("View", "Name"))
        item = self.reservation.horizontalHeaderItem(1)
        item.setText(_translate("View", "Id"))
        item = self.reservation.horizontalHeaderItem(2)
        item.setText(_translate("View", "Busy"))
        item = self.reservation.horizontalHeaderItem(3)
        item.setText(_translate("View", "Op"))
        item = self.reservation.horizontalHeaderItem(4)
        item.setText(_translate("View", "Vj"))
        item = self.reservation.horizontalHeaderItem(5)
        item.setText(_translate("View", "Vk"))
        item = self.reservation.horizontalHeaderItem(6)
        item.setText(_translate("View", "Qj"))
        item = self.reservation.horizontalHeaderItem(7)
        item.setText(_translate("View", "Qk"))
        item = self.reservation.horizontalHeaderItem(8)
        item.setText(_translate("View", "A"))
        item = self.data_cache.horizontalHeaderItem(0)
        item.setText(_translate("View", "Addr"))
        item = self.data_cache.horizontalHeaderItem(1)
        item.setText(_translate("View", "Value"))
        self.data_cache_t.setText(_translate("View", "Data Cache"))
        self.inst_queue_t.setText(_translate("View", "Instruction Queue"))
        item = self.inst_queue.horizontalHeaderItem(0)
        item.setText(_translate("View", "Addr"))
        item = self.inst_queue.horizontalHeaderItem(1)
        item.setText(_translate("View", "Instruction"))
        self.load_file_2.setTitle(_translate("View", "Load File"))
        self.choose_file.setText(_translate("View", "Choose File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    View = QtWidgets.QMainWindow()
    ui = Ui_View()
    ui.setupUi(View)
    View.show()
    sys.exit(app.exec_())
