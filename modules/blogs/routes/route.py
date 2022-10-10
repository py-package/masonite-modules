from masonite.routes import Route

from modules.blogs.controllers.BlogController import BlogController

ROUTES = [
    Route.get("/blogs", BlogController.show),
]
