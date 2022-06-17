from ..masonite_module import MasoniteModule

ROUTES = []

modules = MasoniteModule.get_modules()

for module in modules:
    ROUTES += getattr(module, "ROUTES")
