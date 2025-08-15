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
from PyQt5.QtCore import (
    Qt,
    QUrl,
)  # Qt used for alignments, QUrl used for embedded youtube player
from PyQt5.QtWebEngineWidgets import QWebEngineView
from FileManager import FileManager


class ScrollableIngredientChecklist(QListWidget):
    def __init__(self, file_manager):
        super().__init__()  # Call parent's __init__ (QListWidget)
        self.file_manager = file_manager
        self.actual_ingredient_list = (
            self.file_manager.return_all_possible_ingredients()
        )
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
            self.addItem(item)  # adds the configured widget item to self


class ScrollableRecipeList(QListWidget):
    def __init__(self, file_manager):
        super().__init__()  # Call parent's __init__ (QListWidget)
        self.file_manager = file_manager
        self.actual_complete_recipe_list = (
            self.file_manager.return_all_complete_recipes()
        )
        for recipe in self.actual_complete_recipe_list:
            item = QListWidgetItem(
                recipe.get("name")
            )  # creates new list widget item with text set to current recipe name
            self.addItem(item)  # adds the configured widget item to self


class EmbeddedYoutubePlayer(QWidget):
    def __init__(self):
        super().__init__()  # Call parent's __init__ (QWidget)
        self.web_viewer = QWebEngineView()
        self.set_youtube_video(
            "https://www.youtube.com/watch?v=w6TS5J8YRA4"
        )  # TODO: video for testing change later

    def set_youtube_video(self, video_url):
        """
        Converts standard YouTube URL from theMealDB into an embed URL and then loads it into the embedded youtube player.
        """
        if "watch?v" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[
                0
            ]  # extracts the video id
            embed_url = f"https://www.youtube.com/embed/{video_id}"
        else:
            embed_url = video_url

        self.web_viewer.setUrl(QUrl(embed_url))


class InstructionBox(QWidget):
    def __init__(self):
        super().__init__()  # Call parent's __init__ (QWidget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()  # Call parent's __init__ (QMainWindow)
        self.file_manager = FileManager()
        self.scrollable_ingredient_checklist = ScrollableIngredientChecklist(
            self.file_manager
        )
        self.scrollable_recipe_list = ScrollableRecipeList(self.file_manager)
        self.embedded_youtube_player = EmbeddedYoutubePlayer()
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
        self.scrollable_ingredient_checklist.setFixedSize(290, 480)  # width, height
        self.scrollable_recipe_list.setFixedSize(290, 480)  # width, height

        # Grid Layout
        grid = QGridLayout()
        grid.addWidget(self.scrollable_ingredient_checklist, 0, 0)  # widget, row, col
        grid.addWidget(self.scrollable_recipe_list, 0, 1)  # widget, row, col
        grid.addWidget(self.embedded_youtube_player.web_viewer, 0, 2)

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
