from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.loginUI import Ui_MainWindow  # importing our generated file
import sys
from socket import *
import hashlib
import pickle

serverName = 'localhost'  # 'servername'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


def displayMessageBox(icon, title, text):  # display message box
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # connecting the clicked signal with btnClicked slot
        self.ui.pushButton.clicked.connect(self.btnClicked)

    def btnClicked(self):
        try:
            # if username field is empty
            if (self.ui.lineEdit.text() == ""):
                displayMessageBox(QMessageBox.Critical,
                                  "Login - Error", "Username is required!")
            # if password field is empty
            elif (self.ui.lineEdit_2.text() == ""):
                displayMessageBox(QMessageBox.Critical,
                                  "Login - Error", "Password is required!")
            else:
                clientSocket.connect((serverName, serverPort))
                username = self.ui.lineEdit.text()
                password = encrypt_string(self.ui.lineEdit_2.text())
                dictionary = {"username": username, "password": password}
                clientSocket.send(pickle.dumps(dictionary))

                # receive validation and display it
                validation = clientSocket.recv(1024)
                validation = validation.decode()
                if (validation):
                    displayMessageBox(QMessageBox.Information,
                                      "Login - Success", "Credentials are correct!")
                else:
                    displayMessageBox(QMessageBox.Critical,
                                      "Login - Error", "Username or Password is incorrect!")

        except Exception as e:
            displayMessageBox(QMessageBox.Critical,
                              "TheQuizzer - Error", str(e))


def main():
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
    # close connection
    clientSocket.close()


if __name__ == '__main__':
    main()
