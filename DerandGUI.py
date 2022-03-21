import Derand
from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()
window.setGeometry(200,200,500,300)
dname = 'Derand-15mar'
window.setWindowTitle('Derand')
window.show()
sys.exit(app.exec_())