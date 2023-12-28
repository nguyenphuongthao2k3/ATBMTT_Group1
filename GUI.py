from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 497)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 531, 441))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.sinh_khoa_title = QtWidgets.QGroupBox(parent=self.groupBox)
        self.sinh_khoa_title.setGeometry(QtCore.QRect(40, 30, 451, 121))
        self.sinh_khoa_title.setAutoFillBackground(True)
        self.sinh_khoa_title.setObjectName("sinh_khoa_title")
        self.label = QtWidgets.QLabel(parent=self.sinh_khoa_title)
        self.label.setGeometry(QtCore.QRect(20, 30, 201, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.sinh_khoa_title)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.sinh_khoa_title)
        self.label_3.setGeometry(QtCore.QRect(350, 30, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.sinh_khoa_title)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.sinh_khoa_title)
        self.label_5.setGeometry(QtCore.QRect(230, 60, 81, 16))
        self.label_5.setObjectName("label_5")
        self.ngau_nhien = QtWidgets.QPushButton(parent=self.sinh_khoa_title)
        self.ngau_nhien.setGeometry(QtCore.QRect(250, 90, 75, 23))
        self.ngau_nhien.setObjectName("ngau_nhien")
        self.sinh_khoa = QtWidgets.QPushButton(parent=self.sinh_khoa_title)
        self.sinh_khoa.setGeometry(QtCore.QRect(350, 90, 75, 23))
        self.sinh_khoa.setObjectName("sinh_khoa")
        self.khoa_bi_mat = QtWidgets.QLineEdit(parent=self.sinh_khoa_title)
        self.khoa_bi_mat.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.khoa_bi_mat.setObjectName("khoa_bi_mat")
        self.khoa_cong_khai = QtWidgets.QLineEdit(parent=self.sinh_khoa_title)
        self.khoa_cong_khai.setGeometry(QtCore.QRect(320, 60, 113, 20))
        self.khoa_cong_khai.setObjectName("khoa_cong_khai")
        self.p = QtWidgets.QLineEdit(parent=self.sinh_khoa_title)
        self.p.setGeometry(QtCore.QRect(250, 30, 51, 20))
        self.p.setObjectName("p")
        self.q = QtWidgets.QLineEdit(parent=self.sinh_khoa_title)
        self.q.setGeometry(QtCore.QRect(370, 30, 51, 20))
        self.q.setObjectName("q")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 160, 451, 131))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_6.setObjectName("label_6")
        self.chon1 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.chon1.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.chon1.setObjectName("chon1")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 70, 51, 16))
        self.label_7.setObjectName("label_7")
        self.xuat_kq1 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.xuat_kq1.setGeometry(QtCore.QRect(210, 100, 101, 23))
        self.xuat_kq1.setObjectName("xuat_kq1")
        self.ky_van_ban = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.ky_van_ban.setGeometry(QtCore.QRect(330, 100, 91, 23))
        self.ky_van_ban.setObjectName("ky_van_ban")
        self.van_ban1 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.van_ban1.setGeometry(QtCore.QRect(70, 30, 251, 20))
        self.van_ban1.setObjectName("van_ban1")
        self.ket_qua1 = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.ket_qua1.setGeometry(QtCore.QRect(70, 70, 351, 20))
        self.ket_qua1.setObjectName("ket_qua1")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 300, 451, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 51, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 51, 16))
        self.label_9.setObjectName("label_9")
        self.chon2 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.chon2.setGeometry(QtCore.QRect(340, 30, 75, 23))
        self.chon2.setObjectName("chon2")
        self.xuat_kq2 = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.xuat_kq2.setGeometry(QtCore.QRect(210, 90, 101, 23))
        self.xuat_kq2.setObjectName("xuat_kq2")
        self.xac_thuc = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.xac_thuc.setGeometry(QtCore.QRect(330, 90, 91, 23))
        self.xac_thuc.setObjectName("xac_thuc")
        self.van_ban2 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.van_ban2.setGeometry(QtCore.QRect(70, 30, 251, 20))
        self.van_ban2.setObjectName("van_ban2")
        self.ket_qua2 = QtWidgets.QLineEdit(parent=self.groupBox_3)
        self.ket_qua2.setGeometry(QtCore.QRect(70, 60, 351, 20))
        self.ket_qua2.setObjectName("ket_qua2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 562, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Demo chữ ký số RSA"))
        self.groupBox.setStyleSheet(_translate("MainWindow", "\n"
         "            QGroupBox {\n"
         "                border: 2px solid #E7162C; /* Viền và màu sắc viền */\n"
         "                border-radius: 5px; /* Độ cong của góc */\n"
         "                margin-top: 10px; /* Khoảng cách từ trên xuống */\n"
         "            }\n"
         "        "))
        self.sinh_khoa_title.setStyleSheet(_translate("MainWindow", "\n"
        "            QGroupBox {\n"
        "                border: 2px solid #4CAF50; /* Viền và màu sắc viền */\n"
        "                border-radius: 5px; /* Độ cong của góc */\n"
        "                margin-top: 10px; /* Khoảng cách từ trên xuống */\n"
        "            }\n"
        "        "))
        self.sinh_khoa_title.setTitle(_translate("MainWindow", "Sinh khoá"))
        self.label.setText(_translate("MainWindow", "1. Chọn 2 số nguyên tố ngẫu nhiên:"))
        self.label_2.setText(_translate("MainWindow", "p"))
        self.label_3.setText(_translate("MainWindow", "q"))
        self.label_4.setText(_translate("MainWindow", "2. Khoá bí mật:"))
        self.label_5.setText(_translate("MainWindow", "Khoá công khai:"))
        self.ngau_nhien.setText(_translate("MainWindow", "Ngẫu nhiên"))
        self.sinh_khoa.setText(_translate("MainWindow", "Sinh khoá"))
        self.groupBox_2.setStyleSheet(_translate("MainWindow", "\n"
       "            QGroupBox {\n"
       "                border: 2px solid #E75CD1; /* Viền và màu sắc viền */\n"
       "                border-radius: 5px; /* Độ cong của góc */\n"
       "                margin-top: 10px; /* Khoảng cách từ trên xuống */\n"
       "            }\n"
       "        "))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ký văn bản"))
        self.label_6.setText(_translate("MainWindow", "Văn bản: "))
        self.chon1.setText(_translate("MainWindow", "Chọn"))
        self.label_7.setText(_translate("MainWindow", "Kết quả:"))
        self.xuat_kq1.setText(_translate("MainWindow", "Xuất kết quả"))
        self.ky_van_ban.setText(_translate("MainWindow", "Ký văn bản"))
        self.groupBox_3.setStyleSheet(_translate("MainWindow", "\n"
       "            QGroupBox {\n"
       "                border: 2px solid #41B6E7; /* Viền và màu sắc viền */\n"
       "                border-radius: 5px; /* Độ cong của góc */\n"
       "                margin-top: 10px; /* Khoảng cách từ trên xuống */\n"
       "            }\n"
       "        "))
        self.groupBox_3.setTitle(_translate("MainWindow", "Xác thực chữ ký"))
        self.label_8.setText(_translate("MainWindow", "Văn bản: "))
        self.label_9.setText(_translate("MainWindow", "Kết quả:"))
        self.chon2.setText(_translate("MainWindow", "Chọn"))
        self.xuat_kq2.setText(_translate("MainWindow", "Xuất kết quả"))
        self.xac_thuc.setText(_translate("MainWindow", "Xác thực"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
