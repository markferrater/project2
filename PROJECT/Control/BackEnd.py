from PROJECT.Model.Database import DB
from PROJECT.View.Main import Login

class control():

    print('this is from backend')
#===================================================Bar graph====================================================================================
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

    #======================================================Bar graph with design=================================================================================
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class StyledBarDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styled Bar Graph")
        self.resize(600, 400)

        # Sample data
        self.data = {
            "STEM": 40,
            "HUMSS": 25,
            "ABM": 20,
            "GAS": 15
        }

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Figure & canvas
        self.figure = Figure(facecolor="#f0f0f0")  # background like CSS
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.show_all()

    def show_all(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111, facecolor="#f0f0f0")  # chart background

        labels = list(self.data.keys())
        values = list(self.data.values())

        # Bar colors
        colors = ['#4CAF50', '#2196F3', '#FFC107', '#F44336']

        # Draw bars with edge color and width
        bars = ax.bar(labels, values, color=colors, edgecolor="#333", linewidth=1.5)

        # Style title & labels
        ax.set_title("Total Students per Strand", fontsize=16, fontweight="bold", color="#333")
        ax.set_ylabel("Number of Students", fontsize=12, color="#333")
        ax.set_xlabel("Strands", fontsize=12, color="#333")

        # Grid lines like CSS
        ax.grid(True, axis='y', linestyle='--', alpha=0.5)

        # Remove top/right borders (like card style)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, height + 0.5, str(height),
                    ha='center', va='bottom', fontsize=10, fontweight='bold', color="#333")

        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = StyledBarDemo()
    w.show()
    sys.exit(app.exec())


