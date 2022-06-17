import os
import inflection
from masonite.commands import Command
from masonite.utils.location import base_path
from masonite.utils.filesystem import get_module_dir, make_full_directory
from masonite.configuration import config


class ModuleCreateCommand(Command):
    """
    Create new module

    module:create
        {name : Name of the module}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def module_path(self):
        module_path = config("modules").get("name", "modules")

        name = inflection.pluralize(self.argument("name")).lower()
        return os.path.join(base_path(), module_path, name)

    def controller_path(self):
        return os.path.join(self.module_path(), "controllers")

    def routes_path(self):
        return os.path.join(self.module_path(), "routes")

    def templates_path(self):
        return os.path.join(self.module_path(), "templates")

    def model_path(self):
        return os.path.join(self.module_path(), "models")

    def render_stub_file(self, stub_file, cls_name):
        module_path = config("modules").get("name", "modules")
        name = self.argument("name")
        singularize_cap = inflection.singularize(name).capitalize()
        singularize_sml = inflection.singularize(name).lower()
        pluralize = inflection.pluralize(name)

        with open(stub_file, "r") as f:
            content = f.read()
            content = content.replace("__class__", cls_name)
            content = content.replace("__singularize_cap__", singularize_cap)
            content = content.replace("__singularize_sml__", singularize_sml)
            content = content.replace("__pluralize__", pluralize)
            content = content.replace("__module__", module_path)
        return content

    def handle(self):
        name = inflection.pluralize(self.argument("name")).lower()
        moduleName = inflection.singularize(name).capitalize()

        make_full_directory(self.controller_path())
        make_full_directory(self.model_path())
        make_full_directory(self.templates_path())
        make_full_directory(self.routes_path())

        controller_content = self.render_stub_file(
            os.path.join(get_module_dir(__file__), "../stubs/controller.skeleton"),
            f"{moduleName}Controller",
        )
        model_content = self.render_stub_file(
            os.path.join(get_module_dir(__file__), "../stubs/model.skeleton"), moduleName
        )
        route_content = self.render_stub_file(
            os.path.join(get_module_dir(__file__), "../stubs/route.skeleton"),
            f"{moduleName}Controller",
        )

        layout_content = self.render_stub_file(
            os.path.join(get_module_dir(__file__), "../stubs/layout.skeleton"),
            f"{moduleName}Layout",
        )
        index_content = self.render_stub_file(
            os.path.join(get_module_dir(__file__), "../stubs/index.skeleton"), f"{moduleName}Index"
        )

        controller_path = os.path.join(self.controller_path(), f"{moduleName}Controller.py")
        with open(controller_path, "w") as f:
            f.write(controller_content)

        model_path = os.path.join(self.model_path(), f"{moduleName}.py")
        with open(model_path, "w") as f:
            f.write(model_content)

        route_path = os.path.join(self.routes_path(), "route.py")
        with open(route_path, "w") as f:
            f.write(route_content)

        layout_path = os.path.join(self.templates_path(), "layout.html")
        index_path = os.path.join(self.templates_path(), "index.html")

        with open(layout_path, "w") as f:
            f.write(layout_content)

        with open(index_path, "w") as f:
            f.write(index_content)

        self.info("Module successfully created!")
