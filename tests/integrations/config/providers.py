from masonite.providers import (
    RouteProvider,
    FrameworkProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    SessionProvider,
    QueueProvider,
    CacheProvider,
    EventProvider,
    StorageProvider,
    HelpersProvider,
    BroadcastProvider,
    AuthenticationProvider,
    AuthorizationProvider,
    HashServiceProvider,
    ORMProvider,
)


from masonite.scheduling.providers import ScheduleProvider
from masonite.notification.providers import NotificationProvider
from masonite.validation.providers import ValidationProvider

# register local package
from src.masonite_modules import ModuleProvider


PROVIDERS = [
    FrameworkProvider,
    HelpersProvider,
    RouteProvider,
    ViewProvider,
    WhitenoiseProvider,
    ExceptionProvider,
    MailProvider,
    NotificationProvider,
    SessionProvider,
    CacheProvider,
    QueueProvider,
    ScheduleProvider,
    EventProvider,
    StorageProvider,
    BroadcastProvider,
    HashServiceProvider,
    AuthenticationProvider,
    ValidationProvider,
    AuthorizationProvider,
    ORMProvider,
]

PROVIDERS += [ModuleProvider]
