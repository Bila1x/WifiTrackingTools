# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Derand.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
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
        MainWindow.resize(800, 643)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Derand_csv = QtGui.QGroupBox(self.centralwidget)
        self.Derand_csv.setGeometry(QtCore.QRect(280, 10, 511, 281))
        self.Derand_csv.setObjectName(_fromUtf8("Derand_csv"))
        self.progressBar = QtGui.QProgressBar(self.Derand_csv)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(10, 250, 491, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.Generate = QtGui.QPushButton(self.Derand_csv)
        self.Generate.setGeometry(QtCore.QRect(390, 20, 75, 23))
        self.Generate.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Generate.setDefault(False)
        self.Generate.setFlat(False)
        self.Generate.setObjectName(_fromUtf8("Generate"))
        self.label_4 = QtGui.QLabel(self.Derand_csv)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.csvDir = QtGui.QLineEdit(self.Derand_csv)
        self.csvDir.setGeometry(QtCore.QRect(50, 20, 311, 20))
        self.csvDir.setText(_fromUtf8("15mar"))
        self.csvDir.setObjectName(_fromUtf8("csvDir"))
        self.csvFile = QtGui.QPlainTextEdit(self.Derand_csv)
        self.csvFile.setEnabled(False)
        self.csvFile.setGeometry(QtCore.QRect(10, 50, 491, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.csvFile.setFont(font)
        self.csvFile.setPlainText(_fromUtf8(""))
        self.csvFile.setObjectName(_fromUtf8("csvFile"))
        self.Derand_Box = QtGui.QGroupBox(self.centralwidget)
        self.Derand_Box.setGeometry(QtCore.QRect(10, 10, 261, 281))
        self.Derand_Box.setObjectName(_fromUtf8("Derand_Box"))
        self.label_3 = QtGui.QLabel(self.Derand_Box)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 46, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.flagSwitch = QtGui.QCheckBox(self.Derand_Box)
        self.flagSwitch.setEnabled(True)
        self.flagSwitch.setGeometry(QtCore.QRect(20, 210, 101, 17))
        self.flagSwitch.setChecked(True)
        self.flagSwitch.setObjectName(_fromUtf8("flagSwitch"))
        self.label_6 = QtGui.QLabel(self.Derand_Box)
        self.label_6.setGeometry(QtCore.QRect(20, 70, 31, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_5 = QtGui.QLabel(self.Derand_Box)
        self.label_5.setGeometry(QtCore.QRect(20, 40, 31, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.MaxDb = QtGui.QSpinBox(self.Derand_Box)
        self.MaxDb.setGeometry(QtCore.QRect(200, 140, 42, 22))
        self.MaxDb.setMinimum(-120)
        self.MaxDb.setMaximum(0)
        self.MaxDb.setProperty("value", -99)
        self.MaxDb.setObjectName(_fromUtf8("MaxDb"))
        self.label_7 = QtGui.QLabel(self.Derand_Box)
        self.label_7.setGeometry(QtCore.QRect(130, 110, 61, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.eq3 = QtGui.QSpinBox(self.Derand_Box)
        self.eq3.setGeometry(QtCore.QRect(70, 170, 42, 22))
        self.eq3.setMaximum(240)
        self.eq3.setProperty("value", 240)
        self.eq3.setObjectName(_fromUtf8("eq3"))
        self.Derand = QtGui.QPushButton(self.Derand_Box)
        self.Derand.setGeometry(QtCore.QRect(140, 210, 101, 31))
        self.Derand.setAutoDefault(True)
        self.Derand.setDefault(True)
        self.Derand.setObjectName(_fromUtf8("Derand"))
        self.eq1 = QtGui.QSpinBox(self.Derand_Box)
        self.eq1.setGeometry(QtCore.QRect(70, 110, 42, 22))
        self.eq1.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.eq1.setMaximum(35)
        self.eq1.setSingleStep(1)
        self.eq1.setProperty("value", 26)
        self.eq1.setObjectName(_fromUtf8("eq1"))
        self.label_9 = QtGui.QLabel(self.Derand_Box)
        self.label_9.setGeometry(QtCore.QRect(130, 140, 61, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.eq2 = QtGui.QSpinBox(self.Derand_Box)
        self.eq2.setGeometry(QtCore.QRect(70, 140, 42, 22))
        self.eq2.setMaximum(100)
        self.eq2.setProperty("value", 60)
        self.eq2.setObjectName(_fromUtf8("eq2"))
        self.label_2 = QtGui.QLabel(self.Derand_Box)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.printDesignated = QtGui.QCheckBox(self.Derand_Box)
        self.printDesignated.setGeometry(QtCore.QRect(20, 230, 70, 17))
        self.printDesignated.setObjectName(_fromUtf8("printDesignated"))
        self.label = QtGui.QLabel(self.Derand_Box)
        self.label.setGeometry(QtCore.QRect(20, 110, 41, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.MaxSNgap = QtGui.QSpinBox(self.Derand_Box)
        self.MaxSNgap.setGeometry(QtCore.QRect(200, 170, 42, 22))
        self.MaxSNgap.setMaximum(500)
        self.MaxSNgap.setProperty("value", 240)
        self.MaxSNgap.setObjectName(_fromUtf8("MaxSNgap"))
        self.MaxAV = QtGui.QSpinBox(self.Derand_Box)
        self.MaxAV.setGeometry(QtCore.QRect(200, 110, 42, 22))
        self.MaxAV.setMinimum(-90)
        self.MaxAV.setMaximum(-1)
        self.MaxAV.setProperty("value", -65)
        self.MaxAV.setObjectName(_fromUtf8("MaxAV"))
        self.label_8 = QtGui.QLabel(self.Derand_Box)
        self.label_8.setGeometry(QtCore.QRect(130, 170, 61, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.start = QtGui.QLineEdit(self.Derand_Box)
        self.start.setGeometry(QtCore.QRect(70, 40, 171, 20))
        self.start.setText(_fromUtf8("9251"))
        self.start.setObjectName(_fromUtf8("start"))
        self.flg = QtGui.QLineEdit(self.Derand_Box)
        self.flg.setGeometry(QtCore.QRect(70, 70, 171, 20))
        self.flg.setText(_fromUtf8("0,4,8,1,26,8,7,11,8,9"))
        self.flg.setObjectName(_fromUtf8("flg"))
        self.Result = QtGui.QPlainTextEdit(self.centralwidget)
        self.Result.setEnabled(False)
        self.Result.setGeometry(QtCore.QRect(10, 300, 781, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Result.setFont(font)
        self.Result.setPlainText(_fromUtf8(""))
        self.Result.setObjectName(_fromUtf8("Result"))
        self.Derand_Box.raise_()
        self.Derand_csv.raise_()
        self.Result.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        #self.Derand.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.Derand.clicked.connect(lambda: self.on_click())
        self.Generate.clicked.connect(lambda: self.generate())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.start, self.flg)
        MainWindow.setTabOrder(self.flg, self.eq1)
        MainWindow.setTabOrder(self.eq1, self.eq2)
        MainWindow.setTabOrder(self.eq2, self.eq3)
        MainWindow.setTabOrder(self.eq3, self.MaxAV)
        MainWindow.setTabOrder(self.MaxAV, self.MaxDb)
        MainWindow.setTabOrder(self.MaxDb, self.MaxSNgap)
        MainWindow.setTabOrder(self.MaxSNgap, self.printDesignated)
        MainWindow.setTabOrder(self.printDesignated, self.Generate)
        MainWindow.setTabOrder(self.Generate, self.flagSwitch)
        MainWindow.setTabOrder(self.flagSwitch, self.Derand)
        MainWindow.setTabOrder(self.Derand, self.csvDir)
        MainWindow.setTabOrder(self.csvDir, self.Result)
        MainWindow.setTabOrder(self.Result, self.csvFile)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.Derand_csv.setTitle(_translate("MainWindow", "Derand csv", None))
        self.Generate.setText(_translate("MainWindow", "Generate", None))
        self.label_4.setText(_translate("MainWindow", "File:", None))
        self.Derand_Box.setTitle(_translate("MainWindow", "Derand", None))
        self.label_3.setText(_translate("MainWindow", "eq3", None))
        self.flagSwitch.setText(_translate("MainWindow", "Consider flags", None))
        self.label_6.setText(_translate("MainWindow", "Flags:", None))
        self.label_5.setText(_translate("MainWindow", "Start:", None))
        self.label_7.setText(_translate("MainWindow", "MaxAV:", None))
        self.Derand.setText(_translate("MainWindow", "&Derand", None))
        self.label_9.setText(_translate("MainWindow", "MaxDb:", None))
        self.label_2.setText(_translate("MainWindow", "eq2", None))
        self.printDesignated.setText(_translate("MainWindow", "ShowAppl", None))
        self.label.setText(_translate("MainWindow", "eq1", None))
        self.label_8.setText(_translate("MainWindow", "MaxSNgap:", None))


    def on_click(self):
        #textbval = self.Derand.text()
        Derand.dname = "Derand-" + self.csvDir.text()
        Derand.start = int(self.start.text())
        #Derand.showAppl = int(self.???.text())
        Derand.MaxAV = int(self.MaxAV.text())
        Derand.MaxSNgap = int(self.MaxSNgap.text())
        Derand.flags = self.flg.text()
        Derand.MaxDb = int(self.MaxDb.text())
        Derand.after = ''
        Derand.eq1 = self.eq1.value()
        Derand.eq2 = self.eq2.value()
        Derand.eq3 = self.eq3.value()
        Derand.magic()
        self.Result.setEnabled(True)
        self.Result.setPlainText(Derand.toGUI)
        #print(Derand.result)

    def generate(self):
        Derand.cap = self.csvDir.text()
        Derand.dname = "Derand-" + self.csvDir.text()
        Derand.makeDlist()
        self.progressBar.setValue(0)
        if type(Derand.p) is not int:
            progTime = time.time()
            while True:
                if Derand.p.poll() is not None:
                    break
                self.progressBar.setValue((time.time() - progTime) / (0.50 * Derand.capSize) * 100)
                app.processEvents()
                time.sleep(0.1)
            while Derand.p.poll() is None:
                app.processEvents()
                time.sleep(0.1)

        self.progressBar.setValue(0)
        Derand.openShark()
        self.csvFile.setEnabled(True)
        self.csvFile.setPlainText(Derand.dlist)
        print(Derand.capSize)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())