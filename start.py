import sys
from PyQt4 import QtCore, QtGui
sys.path.append('./forms')
from MainWindow import MainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())
