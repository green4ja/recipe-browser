import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QListWidget,
    QListWidgetItem,
    QCheckBox,
)
from PyQt5.QtGui import QIcon, QFont  # QIcon used for window icon, QFont used for fonts
from PyQt5.QtCore import Qt  # Qt used for alignments
from FileManager import FileManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.FileManager = FileManager()
        self.setWindowTitle("recipe-browser")  # set the window title
        self.setGeometry(
            480, 270, 960, 540
        )  # (opening x coordinate, opening y coordinate, window width, window height)
        self.setWindowIcon(
            QIcon("media/window_icon.png")
        )  # set the icon in the top left of the window
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create Ingredient List Widget
        ingredient_list_widget = QListWidget(self)
        actual_ingredient_list = self.FileManager.return_all_possible_ingredients()
        for ingredient in actual_ingredient_list:
            item = QListWidgetItem(
                ingredient
            )  # creates new list widget item with text set to current ingredient name
            item.setFlags(
                item.flags() | Qt.ItemIsUserCheckable
            )  # adds a checkbox to each ingredient
            item.setCheckState(
                Qt.Unchecked
            )  # sets initial state of checkbox to "unchecked"
            ingredient_list_widget.addItem(
                item
            )  # adds the configured widget item to ingredient_list_widget

        # Grid Layout
        grid = QGridLayout()
        grid.addWidget(ingredient_list_widget, 0, 0)  # widget, row, col

        central_widget.setLayout(grid)


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
