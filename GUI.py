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


class ScrollableIngredientChecklist(QListWidget):
    def __init__(self):
        super().__init__()  # Call parent's __init__ (QListWidget)
        self.FileManager = FileManager()
        self.ingredient_list_widget = QListWidget(self)
        self.actual_ingredient_list = self.FileManager.return_all_possible_ingredients()
        for ingredient in self.actual_ingredient_list:
            item = QListWidgetItem(
                ingredient
            )  # creates new list widget item with text set to current ingredient name
            item.setFlags(
                item.flags() | Qt.ItemIsUserCheckable
            )  # adds a checkbox to each ingredient
            item.setCheckState(
                Qt.Checked
            )  # sets initial state of checkbox to "unchecked"
            self.ingredient_list_widget.addItem(
                item
            )  # adds the configured widget item to ingredient_list_widget


class ScrollableRecipeList(QListWidget):
    def __init__(self):
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call parent's __init__ (QMainWindow)
        self.ScrollableIngredientChecklist = ScrollableIngredientChecklist()
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
        scrollable_ingredient_checklist = (
            self.ScrollableIngredientChecklist.ingredient_list_widget
        )
        scrollable_ingredient_checklist.setFixedSize(290, 480)  # width, height

        # Grid Layout
        grid = QGridLayout()
        grid.addWidget(scrollable_ingredient_checklist, 0, 0)  # widget, row, col

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
