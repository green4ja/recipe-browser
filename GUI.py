import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("recipe-browser") # set the window title
        self.setGeometry(710, 290, 500, 500) # (opening x coordinate, opening y coordinate, window width, window height)
        self.setWindowIcon(QIcon("media/window_icon.png")) # set the icon in the top left of the window

def main():
    """
    If GUI.py is ran directly, the code within this function will execute.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
