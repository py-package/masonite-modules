# masonite_modules

<p align="center">
    <img src="https://banners.beyondco.de/masonite_modules.png?theme=light&packageManager=pip+install&packageName=masonite-modules&pattern=topography&style=style_1&description=Modularize your masonite project&md=1&showWatermark=1&fontSize=100px&images=https%3A%2F%2Fgblobscdn.gitbook.com%2Fspaces%2F-L9uc-9XAlqhXkBwrLMA%2Favatar.png">
</p>

<p align="center">
  <a href="https://docs.masoniteproject.com">
    <img alt="Masonite Package" src="https://img.shields.io/static/v1?label=Masonite&message=package&labelColor=grey&color=blue&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAIRlWElmTU0AKgAAAAgABQESAAMAAAABAAEAAAEaAAUAAAABAAAASgEbAAUAAAABAAAAUgEoAAMAAAABAAIAAIdpAAQAAAABAAAAWgAAAAAAAABIAAAAAQAAAEgAAAABAAOgAQADAAAAAQABAACgAgAEAAAAAQAAAA6gAwAEAAAAAQAAAA4AAAAATspU+QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAVlpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KTMInWQAAAnxJREFUKBVNUl1IVEEUPjPObdd1VdxWM0rMIl3bzbVWLSofVm3th0AhMakHHyqRiNSHEAq5b2HSVvoQRUiEECQUQkkPbRslRGigG8auoon2oPSjpev+3PWeZq7eaC5nDt93vplz5txDQJYpNxX4st4JFiwj9aCqmswUFQNS/A2YskrZJPYefkECC2GhQwAqvLYybwXrwBvq8HSNOXRO92+aH7nW8vc/wS2Z9TqneYt2KHjlf9Iv+43wFJMExzO0YE5OKe60N+AOW6OmE+WJTBrg23jjzWxMBauOlfyycsV24F+cH+zAXYUOGl+DaiDxfl245/W9OnVrSY+O2eqPkyz4sVvHoKp9gOihf5KoAVv3hkQgbj/ihG9fI3RixKcUVx7lJVaEc0vnyf2FFll+ny80ZHZiGhIKowWJBCEAKr+FSuNDLt+lxybSF51lo74arqs113dOZqwsptxNs5bwi7Q3q8npSC2AWmvjTncZf1l61e5DEizNn5mtufpsqk5+CZTuq00sP1wkNPv8jeEikVVlJso+GEwRtNs3QeBt2YP2V2ZI3Tx0e+7T89zK5tNASOLEytJAryGtkLc2PcBM5byyUWYkMQpMioYcDcchC6xN220Iv36Ot8pV0454RHLEwmmD7UWfIdX0zq3GjMPG5NKBtv5qiPEPekK2U51j1451BZoc3i+1ohSQ/UzzG5uYFFn2mwVUnO4O3JblXA91T51l3pB3QweDl7sNXMyEjbguSjrPcQNmwDkNc8CbCvDd0+xCC7RFi9wFulD3mJeXqxQevB4prrqgc0TmQ85NG/K43e2UwnMVAJIEBNfWRYR3HfnvivrIzMyo4Hgy+hfscvLo53jItAAAAABJRU5ErkJggg==">
  </a>
  <img alt="GitHub Workflow Status (branch)" src="https://img.shields.io/github/workflow/status/yubarajshrestha/masonite-modules/Test%20Application">
  <img src="https://codecov.io/gh/yubarajshrestha/masonite-modules/branch/main/graph/badge.svg?token="/>
  <img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-modules">
  <img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/yubarajshrestha/masonite-modules?include_prereleases">
  <img alt="License" src="https://img.shields.io/github/license/yubarajshrestha/masonite-modules">
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Introduction

Modularize your masonite project.


## Installation

```bash
pip install masonite-modules
```

## Configuration

Add ModuleProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite_modules import ModuleProvider

# ...
PROVIDERS = [
    # ...
    # Third Party Providers
    ModuleProvider,
    # ...
]
```

Then you can publish the package resources (if needed) by doing:

```bash
python craft package:publish masonite_modules
```

## Usage

We need a modules directory to store our modules. So create a directory called `modules` in your project root:

```bash
$ mkdir modules
```

Now, create a `__init__.py` file in the `modules` directory and add the following to it:

```python
import os
PATH = os.path.dirname(os.path.abspath(__file__))
```

Inside of the `modules` directory, create a directory for each module you want to create.
For example, if you wanted to create a module called `blogs` you would create a directory called `blogs` inside of the `modules` directory. So the directory structure would look like this:

```
modules
└── __init__.py
└── blogs
└── categories
└── ...
```

You'll also need to create a directory called `routes` inside of each module directory. This is where you will put your route. Just create one file inside of the `routes` directory and name it `route.py` or `web.py` or whatever with `.py` ext.

Lastly, your application directory structure will look like this:

```
modules
└── __init__.py
└── blogs
  └── controllers
  └── models
  └── routes
    └── route.py
  └── templates
└── categories
  └── controllers
  └── models
  └── routes
    └── route.py
  └── templates
└── ...
```

**Blogs Module Example**
```python
# modules.blogs.controllers.BlogController.py

from masonite.views import View
from masonite.controllers import Controller

class BlogController(Controller):
    """BlogController Controller Class."""

    def index(self, view: View):
        return view.render("blogs:index")
```

```python
# modules.blogs.routes.route.py
from masonite.routes import Route

from modules.blogs.controllers.BlogController import BlogController

ROUTES = [
    Route.get("/blogs", BlogController.index),
]
```

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## Maintainers

- [Yubaraj Shrestha](https://www.github.com/yubarajshrestha)

## License


masonite_modules is open-sourced software licensed under the [MIT license](LICENSE).

