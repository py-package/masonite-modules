"""A BlogController Module."""
from masonite.views import View
from masonite.controllers import Controller


class BlogController(Controller):
    """BlogController Controller Class."""

    def show(self, view: View):
        return view.render("blogs:index")
