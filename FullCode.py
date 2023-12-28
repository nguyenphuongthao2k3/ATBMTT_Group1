import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from Algorithm import generate_keypair, sign, verify, decrypt, generate_large_prime
from GUI import Ui_MainWindow

public_key, private_key = generate_keypair()

class RSAApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các sự kiện với các hàm xử lý
        self.ui.ngau_nhien.clicked.connect(self.generate_random_primes)
        self.ui.sinh_khoa.clicked.connect(self.generate_keypair)
        self.ui.chon1.clicked.connect(self.load_text_file1)
        self.ui.ky_van_ban.clicked.connect(self.sign_text)
        self.ui.xuat_kq1.clicked.connect(self.export_signed_text)
        self.ui.chon2.clicked.connect(self.load_text_file2)
        self.ui.xac_thuc.clicked.connect(self.verify_signature)
        self.ui.xuat_kq2.clicked.connect(self.export_decrypted_text)

    def generate_random_primes(self):
        p = generate_large_prime()
        q = generate_large_prime()
        self.ui.p.setText(str(p))
        self.ui.q.setText(str(q))

    def generate_keypair(self):
        self.ui.khoa_bi_mat.setText(str(private_key[1]))
        self.ui.khoa_cong_khai.setText(str(public_key[1]))

    def load_text_file1(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn file văn bản", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "r") as file:
                text_content = file.read()
                self.ui.van_ban1.setText(text_content)

    def sign_text(self):
        message = int(self.ui.van_ban1.text())
        signature = sign(message, private_key)
        self.ui.ket_qua1.setText(str(signature))

    def export_signed_text(self):
        signature = int(self.ui.ket_qua1.text())
        file_name, _ = QFileDialog.getSaveFileName(self, "Xuất kết quả", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(str(signature))

    def load_text_file2(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Chọn file văn bản", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "r") as file:
                text_content = file.read()
                self.ui.van_ban2.setText(text_content)

    def verify_signature(self):
        messenger = int(self.ui.van_ban1.text())
        signature = int(self.ui.van_ban2.text())
        verification_result = verify(messenger, signature, public_key)
        if verification_result:
            decrypted_message = decrypt(signature, public_key)
            self.ui.ket_qua2.setText(str(decrypted_message))
            QMessageBox.information(self, "Xác thực", "Xác thực thành công!")
        else:
            QMessageBox.warning(self, "Xác thực", "Xác thực không thành công!")

    def export_decrypted_text(self):
        decrypted_message = int(self.ui.ket_qua2.text())
        file_name, _ = QFileDialog.getSaveFileName(self, "Xuất kết quả", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "w") as file:
                file.write(str(decrypted_message))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = RSAApp()
    mainWindow.show()
    sys.exit(app.exec())
