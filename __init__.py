from .settings import Settings
del settings
from ._version import __version__
print(f"ezsettings version: {__version__}")
