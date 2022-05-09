# Show site information

from .window import SiteInfoWindow

# this_window is the export that the host application uses
# TODO: be lazy instead of instantiating when the plugin is loaded
this_window = SiteInfoWindow()

# a callable that runs when the button in the main window
# gets clicked
clicked_function = this_window.clicked
