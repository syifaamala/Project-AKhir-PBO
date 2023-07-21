from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(654, 594)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("background-color:rgba(0,0,0,80);\n"
        "border-top-left-radius: 50px;")
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(270, 30, 240, 430))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
        "border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(340, 80, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.user = QtWidgets.QLineEdit(self.widget)
        self.user.setGeometry(QtCore.QRect(295, 150, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.user.setFont(font)
        self.user.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                "border:none;\n"
                "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                "color:rgba(0, 0, 0, 240);\n"
                "padding-bottom:7px;")
        self.user.setObjectName("user")
        self.sandi = QtWidgets.QLineEdit(self.widget)
        self.sandi.setGeometry(QtCore.QRect(295, 215, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sandi.setFont(font)
        self.sandi.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
                "border:none;\n"
                "border-bottom:2px solid rgba(46, 82, 101, 200);\n"
                "color:rgba(0, 0, 0, 240);\n"
                "padding-bottom:7px;")
        self.sandi.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sandi.setObjectName("sandi")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(295, 295, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                " background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "color:rgba(255, 255, 255, 210);\n"
                "border-radius:5px;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:hover{\n"
                "  background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 255));\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " background-color:rgba(150, 123, 111, 255);\n"
                "}\n"
                "\n"
                "")
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(290, 350, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.label_5.setObjectName("label_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(320, 380, 141, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton#pushButton{\n"
                " background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "color:rgba(255, 255, 255, 210);\n"
                "border-radius:5px;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:hover{\n"
                "  background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 255));\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " background-color:rgba(150, 123, 111, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                " background-color: rgba(0, 0, 0, 0);\n"
                "color:rgba(85, 98, 112, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                "  color: rgba(131, 96, 53, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " color:rgba(91, 88, 53, 255);\n"
                "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton#pushButton{\n"
                " background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "color:rgba(255, 255, 255, 210);\n"
                "border-radius:5px;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:hover{\n"
                "  background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 255));\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " background-color:rgba(150, 123, 111, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                " background-color: rgba(0, 0, 0, 0);\n"
                "color:rgba(85, 98, 112, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                "  color: rgba(131, 96, 53, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " color:rgba(91, 88, 53, 255);\n"
                "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton#pushButton{\n"
                " background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "color:rgba(255, 255, 255, 210);\n"
                "border-radius:5px;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:hover{\n"
                "  background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 255));\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " background-color:rgba(150, 123, 111, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                " background-color: rgba(0, 0, 0, 0);\n"
                "color:rgba(85, 98, 112, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                "  color: rgba(131, 96, 53, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " color:rgba(91, 88, 53, 255);\n"
                "}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton#pushButton{\n"
                " background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
                "color:rgba(255, 255, 255, 210);\n"
                "border-radius:5px;\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:hover{\n"
                "  background-color: qlineargradient(spread:pad, x1:0.339011, y1:0.472, x2:0.99435, y2:0.983, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 255));\n"
                "}\n"
                "\n"
                "QPushButton#pushButton:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " background-color:rgba(150, 123, 111, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
                " background-color: rgba(0, 0, 0, 0);\n"
                "color:rgba(85, 98, 112, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
                "  color: rgba(131, 96, 53, 255);\n"
                "}\n"
                "\n"
                "QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
                " padding-left:5px;\n"
                " padding-top:5px;\n"
                " color:rgba(91, 88, 53, 255);\n"
                "}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 80, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(50, 90, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(50, 120, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 160, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")
        self.alert = QtWidgets.QLabel(self.widget)
        self.alert.setGeometry(QtCore.QRect(300, 260, 220, 20))
        self.alert.setText("")
        self.alert.setObjectName("alert")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.sandi.clear) # type: ignore
        self.pushButton.clicked.connect(self.user.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "l"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.user.setPlaceholderText(_translate("Form", "Username"))
        self.sandi.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.label_5.setText(_translate("Form", "Forgot your Username or Password?"))
        self.pushButton_2.setText(_translate("Form", "E"))
        self.pushButton_3.setText(_translate("Form", "D"))
        self.pushButton_4.setText(_translate("Form", "M"))
        self.pushButton_5.setText(_translate("Form", "C"))
        self.label_7.setText(_translate("Form", "Syifa , Ervina"))
        self.label_9.setText(_translate("Form", "Azza & Najla"))
        self.label_8.setText(_translate("Form", "Hi, \n"
"Welcome to our channel.\n"
""))

        self.sandi.setEchoMode(QtWidgets.QLineEdit.Password) #membuat password ketika diketik menjadi bintang ****
        self.pushButton.clicked.connect(self.proses) #signal

    def proses(self): #slot
        username = self.user.text() #user = nama objek QlineEdit yang menampung user
        password = self.sandi.text() #sandi = nama objek QlineEdit yang menampung password
        # Cek login disini
        if len(username) == 0 or len(password)==0: # mengecek jika kolom user/ pass kosong
                self.alert.setText("User dan password wajib diisi") 
        elif username == "admin" and password == "admin123":
                QMessageBox.information(None, "Login Berhasil", "Anda berhasil login") 
        else:
                self.alert.setText("username atau password salah!")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
