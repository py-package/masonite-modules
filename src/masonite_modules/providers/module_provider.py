"""A ModuleProvider Service Provider."""

from masonite.packages import PackageProvider

from ..masonite_module import MasoniteModule


class ModuleProvider(PackageProvider):
    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("masonite_modules")
            .name("modules")
            .config("config/modules.py", publish=True)
            .routes("routes/route.py")
        )

    def register(self):
        super().register()
        MasoniteModule(self.application).register()

    def boot(self):
        """Boots services required by the container."""
        pass
