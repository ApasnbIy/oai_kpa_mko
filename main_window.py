# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1197, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(750, 0))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 578))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.DltUnitPButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DltUnitPButt.sizePolicy().hasHeightForWidth())
        self.DltUnitPButt.setSizePolicy(sizePolicy)
        self.DltUnitPButt.setObjectName("DltUnitPButt")
        self.gridLayout.addWidget(self.DltUnitPButt, 1, 0, 1, 1)
        self.DltUnitNumSBox = QtWidgets.QSpinBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DltUnitNumSBox.sizePolicy().hasHeightForWidth())
        self.DltUnitNumSBox.setSizePolicy(sizePolicy)
        self.DltUnitNumSBox.setMinimumSize(QtCore.QSize(50, 0))
        self.DltUnitNumSBox.setObjectName("DltUnitNumSBox")
        self.gridLayout.addWidget(self.DltUnitNumSBox, 1, 1, 1, 1)
        self.AddUnitPButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddUnitPButt.sizePolicy().hasHeightForWidth())
        self.AddUnitPButt.setSizePolicy(sizePolicy)
        self.AddUnitPButt.setMinimumSize(QtCore.QSize(150, 0))
        self.AddUnitPButt.setObjectName("AddUnitPButt")
        self.gridLayout.addWidget(self.AddUnitPButt, 0, 0, 1, 2)
        self.DltAllUnitsPButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DltAllUnitsPButt.sizePolicy().hasHeightForWidth())
        self.DltAllUnitsPButt.setSizePolicy(sizePolicy)
        self.DltAllUnitsPButt.setMinimumSize(QtCore.QSize(150, 0))
        self.DltAllUnitsPButt.setObjectName("DltAllUnitsPButt")
        self.gridLayout.addWidget(self.DltAllUnitsPButt, 2, 0, 1, 2)
        self.LoadCfgPButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LoadCfgPButt.sizePolicy().hasHeightForWidth())
        self.LoadCfgPButt.setSizePolicy(sizePolicy)
        self.LoadCfgPButt.setMinimumSize(QtCore.QSize(150, 0))
        self.LoadCfgPButt.setObjectName("LoadCfgPButt")
        self.gridLayout.addWidget(self.LoadCfgPButt, 4, 0, 1, 2)
        self.SaveCfgPButt = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveCfgPButt.sizePolicy().hasHeightForWidth())
        self.SaveCfgPButt.setSizePolicy(sizePolicy)
        self.SaveCfgPButt.setMinimumSize(QtCore.QSize(150, 0))
        self.SaveCfgPButt.setObjectName("SaveCfgPButt")
        self.gridLayout.addWidget(self.SaveCfgPButt, 5, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 3, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.DataTable = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DataTable.sizePolicy().hasHeightForWidth())
        self.DataTable.setSizePolicy(sizePolicy)
        self.DataTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DataTable.setRowCount(20)
        self.DataTable.setObjectName("DataTable")
        self.DataTable.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.DataTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.DataTable.setHorizontalHeaderItem(1, item)
        self.DataTable.horizontalHeader().setCascadingSectionResizes(False)
        self.DataTable.horizontalHeader().setDefaultSectionSize(150)
        self.DataTable.horizontalHeader().setMinimumSectionSize(50)
        self.DataTable.horizontalHeader().setStretchLastSection(True)
        self.DataTable.verticalHeader().setDefaultSectionSize(25)
        self.horizontalLayout.addWidget(self.DataTable)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DltUnitPButt.setText(_translate("MainWindow", "Удалить"))
        self.AddUnitPButt.setText(_translate("MainWindow", "Добавить"))
        self.DltAllUnitsPButt.setText(_translate("MainWindow", "Удалить все"))
        self.LoadCfgPButt.setText(_translate("MainWindow", "Загрузить"))
        self.SaveCfgPButt.setText(_translate("MainWindow", "Сохранить"))
        item = self.DataTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.DataTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Значение"))

