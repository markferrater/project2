import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PROJECT.Model.Database import DB   #For mysql database
from PROJECT.Control.BackEnd import DB  #For system logic and communicate to the database
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFormLayout, QLineEdit, \
    QMessageBox, QCheckBox


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(400,360)
        #self.setFixedSize(450, 450)
        self.setStyleSheet("Background: white")

        # ===========================Main layout================================
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(12, 12, 12, 12)

        #==================First layout (main layout login)=====================
        logo_layout = QVBoxLayout()
        img = QPixmap("Logo.png")
        label = QLabel()
        label.setPixmap(img)
        label.setPixmap(img.scaled(130,132 , Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)


        logo_layout.addWidget(label)
        main_layout.addLayout(logo_layout)

        # ==================Second layout (main layout login)=====================
        form_card = QWidget()
        form_card.setStyleSheet("""
        background-color: #D4D5FF;
        border-radius: 10px;
        border: 1px solid black;
        height: 48px;
        padding: 20px;
        """)

        form_layout = QFormLayout(form_card)

        self.input1 = QLineEdit()
        self.input1.setPlaceholderText('Ex: jhon')
        self.input1.setStyleSheet("""
        background-color: white;
        border: 1px;
        padding: 5px;
        """)

        self.input2 = QLineEdit()
        self.input2.setPlaceholderText('Ex: pass123')
        self.input2.setEchoMode(QLineEdit.EchoMode.Password)
        self.input2.setStyleSheet("""
                background-color: white;
                border: solid, 1px;
                padding: 5px;
                """)

        label_name = QLabel('Username')
        label_name.setStyleSheet("""
        padding: 2px;
        border: none;
        """)
        label_password = QLabel('Password')
        label_password.setStyleSheet("""
        padding: 2px;
        border: none;
        """)

        form_layout.addRow(label_name)
        form_layout.addRow(self.input1)

        form_layout.addRow(label_password)
        form_layout.addRow(self.input2)


        self.btn = QPushButton('Submit')
        self.btn.clicked.connect(self.next)

        self.show_pass = QCheckBox("Show Password")
        self.show_pass.stateChanged.connect(self.toggle_password)
        self.show_pass.setStyleSheet("""
        border: none;
        padding: 0px
        """)
        self.btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.btn.setStyleSheet(""" 
        QPushButton {
        background-color: #f0f735;
        border: 1px;
        font: bold;
        border-radius: 10px;
        padding: 5px;
        font-size: 14px;
        cursor: pointer;
        }
        
        QPushButton:hover {
        background-color: #fbff9a;
        }
        
        QPushButton:pressed {
        background-color: #868931;
        
        }
    """)

        form_layout.addWidget(self.show_pass)
        form_layout.addWidget(self.btn)
        main_layout.addWidget(form_card)

        # ==================Main window adding the main layout=====================
        self.setLayout(main_layout)

    def toggle_password(self):
        if self.show_pass.isChecked():
            self.input2.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.input2.setEchoMode(QLineEdit.EchoMode.Password)

    def next(self):
        username = self.input1.text()
        password = self.input2.text()

        if username == "" or password == "":
            x = "Please fill in all required fields!"
            self.show_warning(x)

        elif username == "jhon" and password == "123":
            self.d = Dashboard()
            self.d.show()
            self.close()

        else:
            a = "Invalid username or password!"
            self.show_warning(a)

    def show_warning(self, a):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Warning")
        msg.setText(a)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')
        self.showMaximized()

        #==================Main layout==================
        main_layout = QVBoxLayout()

        # ==================Adding main layout to dashboard==================
        self.setLayout(main_layout)




if __name__ == '__main__':
    app = QApplication([])
    w = Login()
    w.show()
    sys.exit(app.exec())


