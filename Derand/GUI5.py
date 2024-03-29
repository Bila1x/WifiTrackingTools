# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DerandTable.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

# from PyQt4 import QtCore, QtGui
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import Derand
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(950, 632)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.Result = QtGui.QPlainTextEdit(self.centralwidget)
        self.Result.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Result.sizePolicy().hasHeightForWidth())
        self.Result.setSizePolicy(sizePolicy)
        self.Result.setMinimumSize(QtCore.QSize(0, 300))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Courier New")
        self.Result.setFont(font)
        self.Result.setPlainText(_fromUtf8(""))
        self.Result.setObjectName(_fromUtf8("Result"))
        self.gridLayout_3.addWidget(self.Result, 1, 0, 1, 2)
        self.Derand_csv = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Derand_csv.sizePolicy().hasHeightForWidth())
        self.Derand_csv.setSizePolicy(sizePolicy)
        self.Derand_csv.setMaximumSize(QtCore.QSize(16777215, 400))
        self.Derand_csv.setObjectName(_fromUtf8("Derand_csv"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Derand_csv)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.progressBar = QtGui.QProgressBar(self.Derand_csv)
        self.progressBar.setEnabled(True)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMaximum(500)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.gridLayout_2.addWidget(self.progressBar, 1, 0, 1, 1)

        self.model = QtGui.QStandardItemModel(self.Derand_csv)
        self.tableView = QtGui.QTableView(self.Derand_csv)
        self.tableView.setModel(self.model)
        self.tableView.horizontalHeader().setStretchLastSection(True)


        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.Derand_csv, 0, 1, 1, 1)
        self.Derand_Box = QtGui.QGroupBox(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Derand_Box.sizePolicy().hasHeightForWidth())
        self.Derand_Box.setSizePolicy(sizePolicy)
        self.Derand_Box.setMinimumSize(QtCore.QSize(220, 0))
        self.Derand_Box.setMaximumSize(QtCore.QSize(220, 400))
        self.Derand_Box.setObjectName(_fromUtf8("Derand_Box"))
        self.verticalLayout = QtGui.QVBoxLayout(self.Derand_Box)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_4 = QtGui.QLabel(self.Derand_Box)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.csvDir = QtGui.QLineEdit(self.Derand_Box)
        self.csvDir.setText(_fromUtf8("6oct"))
        self.csvDir.setObjectName(_fromUtf8("csvDir"))
        self.horizontalLayout.addWidget(self.csvDir)
        self.Generate = QtGui.QPushButton(self.Derand_Box)
        self.Generate.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Generate.setDefault(False)
        self.Generate.setFlat(False)
        self.Generate.setObjectName(_fromUtf8("Generate"))
        self.horizontalLayout.addWidget(self.Generate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(self.Derand_Box)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.start = QtGui.QLineEdit(self.Derand_Box)
        self.start.setObjectName(_fromUtf8("start"))
        self.gridLayout.addWidget(self.start, 0, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.Derand_Box)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.flg = QtGui.QLineEdit(self.Derand_Box)
        self.flg.setObjectName(_fromUtf8("flg"))
        self.gridLayout.addWidget(self.flg, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_8 = QtGui.QLabel(self.Derand_Box)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_5.addWidget(self.label_8, 2, 2, 1, 1)
        self.MaxSNgap = QtGui.QSpinBox(self.Derand_Box)
        self.MaxSNgap.setMaximum(500)
        self.MaxSNgap.setProperty("value", 240)
        self.MaxSNgap.setObjectName(_fromUtf8("MaxSNgap"))
        self.gridLayout_5.addWidget(self.MaxSNgap, 2, 3, 1, 1)
        self.label = QtGui.QLabel(self.Derand_Box)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.MaxAV = QtGui.QSpinBox(self.Derand_Box)
        self.MaxAV.setMinimum(-90)
        self.MaxAV.setMaximum(-1)
        self.MaxAV.setProperty("value", -75)
        self.MaxAV.setObjectName(_fromUtf8("MaxAV"))
        self.gridLayout_5.addWidget(self.MaxAV, 0, 3, 1, 1)
        self.eq1 = QtGui.QSpinBox(self.Derand_Box)
        self.eq1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.eq1.setMaximum(35)
        self.eq1.setSingleStep(1)
        self.eq1.setProperty("value", Derand.eq1)
        self.eq1.setObjectName(_fromUtf8("eq1"))
        self.gridLayout_5.addWidget(self.eq1, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.Derand_Box)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_5.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.Derand_Box)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)
        self.eq2 = QtGui.QSpinBox(self.Derand_Box)
        self.eq2.setMaximum(100)
        self.eq2.setProperty("value", Derand.eq2)
        self.eq2.setObjectName(_fromUtf8("eq2"))
        self.gridLayout_5.addWidget(self.eq2, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.Derand_Box)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_5.addWidget(self.label_9, 1, 2, 1, 1)
        self.MaxDb = QtGui.QSpinBox(self.Derand_Box)
        self.MaxDb.setMinimum(-120)
        self.MaxDb.setMaximum(0)
        self.MaxDb.setProperty("value", -99)
        self.MaxDb.setObjectName(_fromUtf8("MaxDb"))
        self.gridLayout_5.addWidget(self.MaxDb, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.Derand_Box)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_5.addWidget(self.label_3, 2, 0, 1, 1)
        self.eq3 = QtGui.QSpinBox(self.Derand_Box)
        self.eq3.setMaximum(240)
        self.eq3.setProperty("value", Derand.eq3)
        self.eq3.setObjectName(_fromUtf8("eq3"))
        self.gridLayout_5.addWidget(self.eq3, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.flagSwitch = QtGui.QCheckBox(self.Derand_Box)
        self.flagSwitch.setEnabled(True)
        self.flagSwitch.setChecked(True)
        self.flagSwitch.setObjectName(_fromUtf8("flagSwitch"))
        self.verticalLayout.addWidget(self.flagSwitch)
        self.printDesignated = QtGui.QCheckBox(self.Derand_Box)
        self.printDesignated.setObjectName(_fromUtf8("printDesignated"))
        self.verticalLayout.addWidget(self.printDesignated)
        self.Derand = QtGui.QPushButton(self.Derand_Box)
        self.Derand.setAutoDefault(True)
        self.Derand.setDefault(True)
        self.Derand.setObjectName(_fromUtf8("Derand"))
        self.verticalLayout.addWidget(self.Derand)
        self.flagSwitch.raise_()
        self.Derand.raise_()
        self.printDesignated.raise_()
        self.gridLayout_3.addWidget(self.Derand_Box, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.Derand.clicked.connect(lambda: self.on_click())
        self.Generate.clicked.connect(lambda: self.generate())


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.csvDir, self.Generate)
        MainWindow.setTabOrder(self.Generate, self.start)
        MainWindow.setTabOrder(self.start, self.flg)
        MainWindow.setTabOrder(self.flg, self.eq1)
        MainWindow.setTabOrder(self.eq1, self.eq2)
        MainWindow.setTabOrder(self.eq2, self.eq3)
        MainWindow.setTabOrder(self.eq3, self.MaxAV)
        MainWindow.setTabOrder(self.MaxAV, self.MaxDb)
        MainWindow.setTabOrder(self.MaxDb, self.MaxSNgap)
        MainWindow.setTabOrder(self.MaxSNgap, self.flagSwitch)
        MainWindow.setTabOrder(self.flagSwitch, self.Derand)
        MainWindow.setTabOrder(self.Derand, self.tableView)
        MainWindow.setTabOrder(self.tableView, self.Result)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Derand_csv.setTitle(_translate("MainWindow", "Derand csv", None))
        self.Derand_Box.setTitle(_translate("MainWindow", "Derand", None))
        self.label_4.setText(_translate("MainWindow", "File:   ", None))
        self.Generate.setText(_translate("MainWindow", "Generate", None))
        self.label_5.setText(_translate("MainWindow", "Start:", None))
        self.label_6.setText(_translate("MainWindow", "Flags:", None))
        self.label_8.setText(_translate("MainWindow", "MaxSNgap:", None))
        self.label.setText(_translate("MainWindow", "eq1", None))
        self.label_7.setText(_translate("MainWindow", "MaxAV:", None))
        self.label_2.setText(_translate("MainWindow", "eq2", None))
        self.label_9.setText(_translate("MainWindow", "MaxDb:", None))
        self.label_3.setText(_translate("MainWindow", "eq3", None))
        self.flagSwitch.setText(_translate("MainWindow", "Consider flags", None))
        self.printDesignated.setText(_translate("MainWindow", "ShowAppl", None))
        self.Derand.setText(_translate("MainWindow", "&Derand", None))

    def showdialog(self):
        msg = QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Critical)

        msg.setText("cap File not found!")
        #msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Error")
        #msg.setDetailedText("The details are as follows:")
        retval = msg.exec_()

    def on_click(self):
        self.Derand.setEnabled(False)
        Derand.showAppl = self.printDesignated.isChecked()
        self.Result.setPlainText('list out of range!')
        Derand.dname = "Derand-" + self.csvDir.text()
        try:
            Derand.MAC = self.start.text().lower()
        except:
            return
        #Derand.showAppl = int(self.???.text())
        print(Derand.MAC)
        Derand.MaxAV = int(self.MaxAV.text())
        Derand.MaxSNgap = int(self.MaxSNgap.text())
        if not self.flagSwitch.isChecked():
            Derand.flags = ''
        elif self.flg.text():
            Derand.flags = self.flg.text()
        else:
            Derand.flags = Derand.dlist[Derand.start - 1][4]
        Derand.MaxDb = int(self.MaxDb.text())
        Derand.after = ''
        Derand.eq1 = self.eq1.value()
        Derand.eq2 = self.eq2.value()
        Derand.eq3 = self.eq3.value()
        Derand.magic()
        if Derand.start > len(Derand.dlist):
            return
        self.Result.setEnabled(True)
        self.Result.setPlainText(Derand.toGUI)
        self.Derand.setEnabled(True)
        #print(Derand.result)

    def generate(self):
        Derand.cap = self.csvDir.text()
        Derand.dname = "Derand-" + self.csvDir.text()
        Derand.makeDlist()
        if not Derand.capSize:
            #self.progressBar.setValue(100)
            self.showdialog()
            return
        #self.progressBar.setValue(0)
        if type(Derand.p) is not int:
            progTime = time.time()
            while True:
                if Derand.p.poll() is not None:
                    break
                self.progressBar.setValue((time.time() - progTime) / (0.55 * Derand.capSize) * 500)
                app.processEvents()
                time.sleep(0.1)
            while Derand.p.poll() is None:
                app.processEvents()
                time.sleep(0.1)

        self.progressBar.setValue(0)
        Derand.openShark()
        self.tableView.setEnabled(True)
        self.model.clear()
        for row in Derand.dlist:
            row[2] = time.strftime('%H:%M:%S', time.localtime(float(row[2])))
            items = [QtGui.QStandardItem(cell) for cell in row]
            self.model.appendRow(items)
        #print(Derand.capSize)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
