# Field Data Collection plugin architecture example

The USGS field data collection modernization effort needs to incorporate many different scientific disciplines,
different field activities, and different data systems.  18F has recommended using a plugin-based architecture for
this new application in order to account for this complexity.

This gist gives an example of a very small Python and Qt application that demonstrates this architecture.

## Concept

There is a top-level Qt application defined in [main.py](main.py). That application looks in the `plugins/` directory
and loads all of those subdirectories as Python packages called _plugins_. Each plugin exports two items that the host
application needs to interact with it, a window object called `this_window` and a function called `clicked_function`
that runs when the user click a button in the main window to open the plugin.

The top-level application includes some very basic interfaces for plugins to access global information. Each plugin
gets a reference to the top-level application that it can use to access that global information. In this basic example,
there is just a dictionary called `config_info` that plugins can access.