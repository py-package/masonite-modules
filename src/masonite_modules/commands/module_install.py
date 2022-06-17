import os
from masonite.commands import Command
from masonite.utils.location import base_path
from masonite.utils.filesystem import make_directory, render_stub_file, get_module_dir
from masonite.configuration import config


class ModuleInstallCommand(Command):
    """
    Masonite Command Utility

    module:install
        {--f|force=? : Force overriding file if already exists}
    """

    def __init__(self, application):
        super().__init__()
        self.app = application

    def modules_path(self):
        module_path = config("modules").get("name", "modules")
        return os.path.join(base_path(), module_path, "__init__.py")

    def handle(self):
        filepath = self.modules_path()

        make_directory(filepath)

        if os.path.exists(filepath) and not self.option("force"):
            self.warning(
                "Modules path already exists! Run the command with -f (force) to override."
            )
            return -1

        init_path = os.path.join(get_module_dir(__file__), "../stubs/__init__.py")
        content = render_stub_file(init_path, "...")

        with open(filepath, "w") as f:
            f.write(content)

        self.info("Module Successfully installed!")
