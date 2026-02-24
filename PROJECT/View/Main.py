# pip install matplotlib
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout,
                             QLabel, QHBoxLayout, QScrollArea, QSizePolicy, QLineEdit)


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dashboard')

        self.setStyleSheet("background:#f2fafc;")
        self.setWindowIcon(QIcon("Logo.png"))

        # ==================Logo==================
        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setFixedSize(150, 150)

        title = QLabel("Dashboard")
        title.setStyleSheet("font-size:18px; font-weight:bold;")

        log_outbtn = QPushButton("Log Out")
        log_outbtn.setStyleSheet("""
        QPushButton {
            background:#f72d2d;
            font-weight:bold;
            border-radius:15px;
            padding:8px 15px;
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
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # ----- HEADER -----
        header_layout = QHBoxLayout()
        header_layout.addWidget(logo)
        header_layout.addWidget(title)
        header_layout.addStretch()
        header_layout.addWidget(log_outbtn)

        header_cardT = QWidget()
        header_cardT.setStyleSheet("""
         background:#444;
         color:white;
         padding:20px;
         border-radius:15px;
        """)
        header_cardT.setFixedHeight(120)
        header_cardT.setLayout(header_layout)
        main_layout.addWidget(header_cardT)

        # ----- BODY -----
        self.header_cardB = QWidget()
        self.header_cardB.setStyleSheet("""
            background:#635b5a;
            color:white;
            padding:15px;
            border-radius:15px;
        """)
        # IMPORTANT: Make it expand to fill space
        self.header_cardB.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        # Create horizontal layout for left and right panels
        body_layout = QHBoxLayout(self.header_cardB)
        main_layout.addWidget(self.header_cardB, 1)  # Give it stretch factor 1

        # ===== LEFT PANEL (Scrollable student cards) =====
        left_widget = QWidget()
        left_widget.setStyleSheet("""
                            background: white;
                            color:black;
                            padding:15px;
                            border-radius:15px;
                        """)
        left_content = QVBoxLayout(left_widget)

        search_header = QHBoxLayout()
        content_body = QVBoxLayout()

        left_content.addLayout(search_header)
        left_content.addLayout(content_body)

        search_label = QLabel('Search: 🔎')
        search_label.setStyleSheet("""
        margin: 1px;
        """)

        search = QLineEdit()
        search.setPlaceholderText('Search by id or name')
        search.setStyleSheet("""
        border: 1px solid;
        padding: 7px;
        margin-right: 20px;
        border-radius: 10px;
        color:black;
        """)

        search_button = QPushButton('search')
        search_button.setStyleSheet("""
        QPushButton{
         border-radius: 5px;
         border: 1px solid grey;
         width: 55px;
         padding: 8px;
         margin-right: 20px;
        }
        
        QPushButton:hover{
        background-color: black;
        color: white;
        }
        
        QPushButton:pressed{
        background-color: grey;
        color: white;
        }
        
        """)

        search_header.addWidget(search_label)
        search_header.addWidget(search)
        search_header.addWidget(search_button)



        # ======Content body=================
        student_widget = QWidget()
        student_widget.setStyleSheet("""
                    background:grey;
                    color:white;
                    padding:15px;
                    border-radius:15px;
                """)
        student_layout = QVBoxLayout(student_widget)

        # Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Widget inside scroll area
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        # STUDENT DATA
        self.students = [
            {"id": 1001, "name": "Mark", "course": "Computer Science"},
            {"id": 1002, "name": "John", "course": "Engineering"},
            {"id": 1003, "name": "Albert", "course": "Mathematics"},
            {"id": 1004, "name": "Peter", "course": "Physics"},
            {"id": 1005, "name": "Sarah", "course": "Biology"},
            {"id": 1006, "name": "Mike", "course": "Chemistry"},
            {"id": 1007, "name": "Emma", "course": "Literature"},
            {"id": 1008, "name": "David", "course": "History"},
            {"id": 1009, "name": "Lisa", "course": "Art"},
            {"id": 1010, "name": "James", "course": "Music"},
        ]

        for student in self.students:
            print(student["id"], "-", student["name"])


        for i, student in enumerate(self.students):
            student_id = student["id"]
            student_name = student["name"]
            student_course = student["course"]

            label_input = f"ID: {student_id}\nName: {student_name}\nCourse: {student_course}"

            # Create card for each student
            card_row = QWidget()
            card_row.setStyleSheet("""
                           QWidget {
                               background-color: white;
                               border: 2px solid #e0e0e0;
                               border-radius: 12px;
                               margin: 8px;
                               padding: 12px;
                           }
                           QWidget:hover {
                               border-color: #007bff;
                               background-color: #f8f9fa;
                           }
                       """)
            card_row_layout = QHBoxLayout(card_row)

            # Student info label
            label = QLabel(label_input)
            label.setStyleSheet("""
                            QLabel {
                                color: black;
                                font-weight: bold;
                                font-size: 14px;
                                padding: 5px;
                                border: none;
                            }
                        """)
            card_row_layout.addWidget(label, 2)

            # Button
            button = QPushButton(f'View Details')
            button.clicked.connect(lambda checked, index=i: self.clicked(index))
            button.setStyleSheet("""
                            QPushButton {
                                border: 1px solid #007bff;
                                background-color: white;
                                color: #007bff;
                                padding: 8px 15px;
                                border-radius: 5px;
                                font-weight: bold;
                                min-width: 100px;
                            }
                            QPushButton:hover {
                                background-color: #007bff;
                                color: white;
                            }
                        """)
            card_row_layout.addWidget(button)

            scroll_layout.addWidget(card_row)

        scroll_layout.addStretch()
        scroll_area.setWidget(scroll_widget)

        student_layout.addWidget(scroll_area)

        content_body.addWidget(student_widget)





        # ===== Right PANEL =====
        right_widget = QWidget()
        right_widget.setStyleSheet("""
                            background: white;
                            color:black;
                            padding:15px;
                            border-radius:15px;
                        """)

        right_layout = QVBoxLayout(right_widget)

        view_layout = QVBoxLayout()

        l1 = QLabel('Student Details')
        l1.setStyleSheet("""
        font-size:18px; 
        font-weight:bold;
        """)

        self.l2 = QWidget()
        self.l2.setStyleSheet("""
        
        """)
        l2_layout = QVBoxLayout(self.l2)

        l2_label = QLabel('Select student to view details')
        l2_label.setStyleSheet("""
                font-size:18px; 
                font-weight:bold;
                padding: 170px;
                """)
        l2_layout.addWidget(l2_label)

        view_layout.addWidget(l1)




        right_layout.addLayout(view_layout)
        body_layout.addWidget(left_widget, 1)

        body_layout.addWidget(right_widget, 1)

        self.showMaximized()

    def button_clicked(self, num):
        print(f"Button {num} clicked")

    def showDefault(self):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = Dashboard()
    w.show()
    sys.exit(app.exec())
