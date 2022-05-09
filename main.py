from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

import importlib
import os
import sys

from pathlib import Path

PLUGIN_DIR = "plugins"


def get_module(path):
    """Return a python module loaded from path."""
    mod = importlib.import_module(path.name)
    return mod


class ExperimentWindow(QWidget):

    """Main window of the application."""

    def __init__(self):
        super().__init__()
        self.config_info = {}
        self.plugins = []
        self.layout = QVBoxLayout(self)

    def load_plugins(self):
        """Load plugins and attach them to the main window."""

        # find subdirectories that are python packages
        plugin_folder = Path(__file__).parent / PLUGIN_DIR
        sys.path.append(str(plugin_folder))

        subfolders = [f for f in plugin_folder.iterdir() if f.is_dir()]

        for d in subfolders:
            # try to load plugins from each subdirectory
            try:
                self.plugins.append(get_module(d))
            except ImportError:
                pass

        for plugin in self.plugins:
            # Attach a reference to main_window to each plugin
            plugin.this_window.application = self

            # Put buttons for plugin windows in the
            # main_window layout
            button = QPushButton(plugin.__name__)
            button.clicked.connect(plugin.clicked_function)
            self.layout.addWidget(button)

    def load_configuration(self):
        """Load configuration data from disk onto the application."""
        # stub out by loading a static dict here
        self.config_info = {
            "sites": {
                "01": {"name": "Test Site", "id": "01",},
                "02": {"name": "Second test site", "id": "02",},
            }
        }


app = QApplication(sys.argv)

window = ExperimentWindow()

window.load_plugins()
window.load_configuration()

window.show()

app.exec()
