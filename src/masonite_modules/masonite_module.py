import importlib
import glob
from pathlib import Path
from masonite.utils.location import base_path
from os.path import dirname, basename, isfile, join


ROOT_PATH = base_path()
MODULES_PATH = join(ROOT_PATH, 'modules')

class MasoniteModule:
    
    def __init__(self, application):
        self.application = application
    
    @staticmethod
    def get_module_name(module):
        return module.replace(ROOT_PATH, '').replace('.py', '').lstrip('/').replace('/', '.')
    
    @staticmethod
    def get_modules():
        modules = glob.glob(join(MODULES_PATH, "**/routes/*.py"))
        masonite_modules = []
        
        for module in modules:
            if isfile(module):
                masonite_modules += [importlib.import_module(MasoniteModule.get_module_name(module))]
        return masonite_modules
        
    def register(self):
        modules = glob.glob(join(MODULES_PATH, "**/routes/*.py"))
        for module in modules:
            if isfile(module):
                module_path = dirname(module).replace(MODULES_PATH, '').split('/')[1]
                self.application.make("view").add_namespaced_location(
                    module_path, f"modules.{module_path}/templates"
                )