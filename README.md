# Field Data Collection plugin architecture example

The USGS field data collection modernization effort needs to incorporate many
different scientific disciplines, different field activities, and different
data systems.  18F has recommended using a plugin-based architecture for this
new application in order to account for this complexity.

This gist gives an example of a very small Python and Qt application that
demonstrates this architecture.

<img width="565" alt="example application" src="https://user-images.githubusercontent.com/443389/167451145-97d94756-62ad-4b0a-8f0a-cf653ad88856.png">

## Concept

There is a top-level Qt application defined in [main.py](main.py). That
application looks in the [plugins/](plugins) directory and loads all of those
subdirectories as Python packages called _plugins_. Each plugin exports two
items that the host application needs to interact with it, a window object
called `this_window` and a function called `clicked_function` that runs when
the user click a button in the main window to open the plugin.

The top-level application includes some very basic interfaces for plugins to
access global information. Each plugin gets a reference to the top-level
application that it can use to access that global information. In this basic
example, there is just a dictionary called `config_info` that plugins can
access.

## Usage

You need Python and `pipenv` installed on your compute. Create a Python
virtual environment for this application using `pipenv install`. Then run the
application with `pipenv run python ./main.py`.

## Next Steps

This is an extremely basic example. For an actual field application, more
featureful capabilities and interfaces between the host application and
plugins would need to be designed and implemented. 

As an example, a plugin that loads configuration information from disk could
be built to populate the main `config_info` site list. Or that plugin could
load site information from an online data system using API calls.

As another example, a plugin that records data from an activity could store
the results in the host application and a separate plugin could output those
results in an output format that can be loaded into another system.
