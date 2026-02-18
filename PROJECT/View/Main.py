# pip install matplotlib
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
#from PROJECT.Model.Database import DB  # For mysql database
#from PROJECT.Control.BackEnd import DB  # For system logic and communicate to the database
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFormLayout, QLineEdit, \
    QMessageBox, QCheckBox, QHBoxLayout


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')
        self.showMaximized()
        self.setStyleSheet("""
        background:#f2fafc;
        """)

        self.setWindowIcon(QIcon("Logo.png"))

        # ==================Logo==================
        logo = QLabel()
        pixmap = QPixmap("logo.png")

        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setFixedSize(150, 150)

        title = QLabel("Dashboard")
        title.setStyleSheet("""
        font-size:18px;
        font-weight:bold;
        """)

        log_outbtn = QPushButton("Log Out")
        log_outbtn.setStyleSheet("""
        QPushButton {
        background:#f72d2d;
        font-weight:bold;
        border-radius:15px;
        }
        
        QPushButton:hover {
        background: #bd3e3e;
        color:white;
        }
        
        QPushButton:pressed {
        background: #fa8787;
        color: #363433;
        }
        
        """)



        # ==================Main layout==================
        main_layout = QVBoxLayout()

        header_layout = QHBoxLayout() # Header content
        header_layout.addWidget(logo)
        header_layout.addWidget(title)

        header_layout.addStretch()

        header_layout.addWidget(log_outbtn)

        header_cardT = QWidget()
        header_cardT.setStyleSheet("""
         background:#444;
         color:white;
         padding:15px;
         border-radius:15px;
        """)
        header_cardT.setFixedHeight(150)
        header_cardT.setLayout(header_layout)
        main_layout.addWidget(header_cardT,1)


        body_layout = QVBoxLayout() # body content

        header_cardB = QWidget()
        header_cardB.setStyleSheet("""
                 background:#635b5a;
                 color:white;
                 padding:15px;
                 border-radius:15px;
                """)
        header_cardB.setLayout(body_layout)
        main_layout.addWidget(header_cardB,2)


        # ==================Adding two layout for the GUI==================
        main_layout.addWidget(header_cardT)
        main_layout.addLayout(body_layout)

        # ==================Adding main layout to dashboard==================
        self.setLayout(main_layout)


if __name__ == '__main__':
    app = QApplication([])
    w = Dashboard()
    w.show()
    sys.exit(app.exec())

