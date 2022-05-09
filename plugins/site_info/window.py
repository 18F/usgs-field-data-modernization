from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListView,
)
from PyQt6.QtCore import QStringListModel


class SiteInfoWindow(QWidget):

    """Window for diplaying site information."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = None
        self.sites = {}
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QLabel("Site Information"))

        hlayout = QHBoxLayout()

        self.filter_field = QLineEdit()
        hlayout.addWidget(self.filter_field)
        self.search_button = QPushButton("Filter")
        self.search_button.clicked.connect(self.filter_sites)
        hlayout.addWidget(self.search_button)

        self.layout.addLayout(hlayout)

        # self.sites is empty initially
        self.sites_model = QStringListModel(
            [self._site_name(site) for site in self.sites]
        )
        self.sites_list = QListView()
        self.sites_list.setModel(self.sites_model)
        self.layout.addWidget(self.sites_list)

    @staticmethod
    def _site_name(site):
        """Make a display name from a site object."""
        return "{}: {}".format(site["id"], site["name"])

    @staticmethod
    def _site_matches(site, search_term):
        return search_term in site["name"] or search_term in site["id"]

    def clicked(self):
        """Method to run when main UI button is clicked."""
        self.filter_sites()  # refresh the site list before showing
        self.show()

    def filter_sites(self):
        """Filter the site list based on the search field's value."""
        # Start with a full set of sites from the main app
        self.sites = self.application.config_info["sites"]
        search_term = self.filter_field.text()
        self.sites_model.setStringList(
            [
                self._site_name(site)
                for site in self.sites.values()
                if self._site_matches(site, search_term)
            ]
        )
