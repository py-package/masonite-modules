"""A ModuleProvider Service Provider."""

from masonite.packages import PackageProvider
from masonite.views import View

from src.masonite_modules.masonite_module import MasoniteModule

class ModuleProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_modules")
            .name("masonite_modules")
            .config("config/masonite_modules.py", publish=True)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()
        MasoniteModule(self.application).register()

    def boot(self):
        """Boots services required by the container."""
        pass
