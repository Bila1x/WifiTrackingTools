import Derand
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setGeometry(200,200,500,300)
dname = 'Derand-15mar'
window.setWindowTitle('Derand')
window.show()
sys.exit(app.exec_())