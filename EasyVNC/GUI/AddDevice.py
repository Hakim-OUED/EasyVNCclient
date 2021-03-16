
import os
import socket
import ssl

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from EasyVNC.localData.utils import *


class AddDeviceUI(QMainWindow):
    def __init__(self, parent=None):
        """"Initializer."""
        super().__init__(parent)
        self.setWindowTitle("EasyVNC Viewer")

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 700)
        self.lbl_msg = QtWidgets.QLabel(Dialog)
        self.lbl_msg.setGeometry(QtCore.QRect(70, 30, 351, 31))
        self.lbl_msg.setObjectName("label")
        self.lbl_msg.setHidden(True)
        self.lbl_msg.setStyleSheet(
            "QLabel"
            "{"
            "text-align: left;"
            "font-weight: bold;"
            "color : rgb(255, 0, 0);"
            "font-size: 15px;"
            "height: 1em;"
            "width: 2ch;"
            "font-family: Arial"
            "}")

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 650, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 150, 141, 41))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 310, 391, 311))
        self.groupBox.setObjectName("groupBox")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(30, 40, 131, 24))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 90, 141, 24))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 140, 181, 24))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setGeometry(QtCore.QRect(30, 250, 141, 24))
        self.checkBox_4.setObjectName("checkBox_4")
        self.edt_path = QtWidgets.QLineEdit(self.groupBox)
        self.edt_path.setGeometry(QtCore.QRect(80, 200, 261, 33))
        self.edt_path.setText("")
        self.edt_path.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(60, 170, 191, 19))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 131, 111))
        self.label_2.setObjectName("label_2")
        self.edt_mail = QtWidgets.QLineEdit(Dialog)
        self.edt_mail.setGeometry(QtCore.QRect(170, 150, 221, 33))
        self.edt_mail.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 141, 41))
        self.label_4.setObjectName("label_4")
        self.edt_password = QtWidgets.QLineEdit(Dialog)
        self.edt_password.setGeometry(QtCore.QRect(170, 210, 221, 33))
        self.edt_password.setObjectName("lineEdit_3")
        self.edt_name = QtWidgets.QLineEdit(Dialog)
        self.edt_name.setGeometry(QtCore.QRect(170, 260, 221, 33))
        self.edt_name.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 141, 41))
        self.label_5.setObjectName("label_5")

        self.edt_path.setPlaceholderText("/home/device/share")
        self.edt_mail.setPlaceholderText("Identifiant/ mail")
        self.edt_password.setPlaceholderText("Password")
        self.edt_name.setPlaceholderText("Identifant convivial unique")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_msg.setText(_translate("Login",
                                        "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">" +
                                        "Identifiants incorrectes " + "</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "Identifiant:"))
        self.groupBox.setTitle(_translate("Dialog", "Options"))
        self.checkBox.setText(_translate("Dialog", "Stream Video"))
        self.checkBox_2.setText(_translate("Dialog", "Stream Audio"))
        self.checkBox_3.setText(_translate("Dialog", "Dossier Partagé"))
        self.checkBox_4.setText(_translate("Dialog", "Route IP directe"))
        self.label_3.setText(_translate("Dialog", "Chemin du dossier partagé"))
        self.label_2.setText(_translate("Dialog", "Ajouter une Device"))
        self.label_4.setText(_translate("Dialog", "Mot de Passe:"))
        self.label_5.setText(_translate("Dialog", "Identifiant Device:"))

    def accept(self):
        if self.check_credential():
            self.close()
        else:

            self.lbl_msg.setText("Incorrect ID/Password")
            self.lbl_msg.setStyleSheet("color: rgb(255, 0, 0);")
            self.lbl_msg.setHidden(False)

    def check_credential(self):
        self.socket_data = read_socket_data()
        hostname = self.socket_data['hostname']
        port = int(self.socket_data['socket_port'])
        context = ssl.create_default_context()
        cert = os.path.dirname(os.path.realpath(__file__)) + '/../Cert/cert.pem'
        print(cert)
        context.load_verify_locations(cert)
        conn = context.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), server_side=False,
                                   server_hostname=hostname)
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((hostname, port))
        response = conn.recv(2048)
        #print(response.decode())

        self.usermail = self.edt_mail.text()
        self.password = self.edt_password.text()

        req = 3000
        name = self.edt_name.text()
        webcam = 1
        audio = 1
        sharing = 1
        shareDoc = self.edt_path.text()
        adresseIP = "127.0.0.1"
        directIP = 1
        lastConn = ""

        data = str(req) + ";" + str(self.usermail) + ";" + self.password + ";" + name + ";" + str(webcam) + ";" + str(audio) + ";" + str(
            sharing) + ";" + shareDoc + ";" + adresseIP + ";" + str(directIP) + ";" + lastConn

        conn.send(str.encode(data))
        cle = conn.recv(1024)
        end = b"SUCCESSFULL REGISTERED!"

        if not cle.isalpha():
            f = open("./"+name + ".conf", 'wb')  # Open in binary

            while (cle):
                f.write(cle)
                print("reception des données")
                if cle == end:
                    break
                cle = conn.recv(1024)
            f.close()
            response = "Device SUCCESSFULL REGISTERED! You can SignIn"

        print(response)
        conn.close()

        if "incorrect" in response.lower():
            self.lbl_msg.setText(response)
            self.lbl_msg.setStyleSheet("color: rgb(255, 0, 0);")
            self.lbl_msg.setHidden(False)
            return False
        else:
            print(response)
            #response = response.split(";")
            #save_config(response[0], self.usermail, response[1])
            return True


    def interprete_chkbox(self, valeur):
        if(valeur == 0):
            return 0
        else:
            return 1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = AddDeviceUI()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
