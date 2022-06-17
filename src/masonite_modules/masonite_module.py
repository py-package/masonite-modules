import importlib
import glob
from masonite.utils.location import base_path
from os.path import dirname, isfile, join
from .commands.module_create import ModuleCreateCommand
from .commands.module_install import ModuleInstallCommand
from masonite.configuration import config


ROOT_PATH = base_path()


class MasoniteModule:
    def __init__(self, application):
        self.application = application

    @staticmethod
    def get_module_name(module):
        return module.replace(ROOT_PATH, "").replace(".py", "").lstrip("/").replace("/", ".")

    @staticmethod
    def get_modules():
        module_config = config("modules")
        if module_config:
            module_name = module_config.get("name", "modules")
            modules = glob.glob(join(base_path(), module_name, "**/routes/*.py"))
            masonite_modules = []

            for module in modules:
                if isfile(module):
                    masonite_modules += [
                        importlib.import_module(MasoniteModule.get_module_name(module))
                    ]
            return masonite_modules
        return []

    def register(self):
        module_config = config("modules")
        if module_config:
            module_name = module_config.get("name", "modules")
            modules = glob.glob(join(base_path(), module_name, "**/routes/*.py"))
            for module in modules:
                if isfile(module):
                    template_path = (
                        dirname(module).replace(join(base_path(), module_name), "").split("/")[1]
                    )
                    self.application.make("view").add_namespaced_location(
                        template_path, f"{module_name}.{template_path}/templates"
                    )

            self.application.make("commands").add(ModuleInstallCommand(self.application)).add(
                ModuleCreateCommand(self.application)
            )
