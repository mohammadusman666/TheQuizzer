from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.loginUI import Ui_MainWindow  # importing our generated file
import sys

from socket import *
serverName = 'localhost'  # 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()    
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked) # connecting the clicked signal with btnClicked slot
    
    def btnClicked(self):
        try:
            clientSocket.connect((serverName, serverPort))
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Connection with Server successful!")
            msg.setText(self.ui.lineEdit.text())
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("TheQuizzer - Error")
            msg.setText("Connection with Server failed!")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()

def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()