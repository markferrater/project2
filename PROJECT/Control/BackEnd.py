from PROJECT.Model.Database import DB
from PROJECT.View.Main import Login

class control():

    print('this is from backend')
#===============================================================================================================
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class SimpleBarDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SHS Strand Bar Graph")
        self.resize(600, 400)

        # Sample data
        self.data = {
            "STEM": 40,
            "HUMSS": 25,
            "ABM": 20,
            "GAS": 15
        }

        print(self.data.keys())
        print(self.data.values())


        # Layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Figure & Canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        # Draw chart
        self.show_all()

    def show_all(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)

        labels = list(self.data.keys())
        values = list(self.data.values())

        print(labels)
        print(values)

        ax.bar(labels, values, color=['#4CAF50', '#2196F3', '#FFC107', '#F44336'])
        ax.set_title("Total Students per Strand")
        ax.set_ylabel("Number of Students")

        self.canvas.draw()  # Refresh the canvas

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SimpleBarDemo()
    w.show()
    sys.exit(app.exec())
