import subprocess
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os



NAME = "QuartNG"
AUTHOR = "0x4248"
DESCRIPTION = ""


def get_git_ref():
	try:
		return subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip().decode("utf-8")
	except subprocess.CalledProcessError:
		return "unknown"

VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0
VERSION_REF = get_git_ref()
VERSION_TYPE = "beta"
VERSION_CODE = "Lonely Lancer"
VERSION = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
VERSION_FULL = f"{VERSION}-{VERSION_REF} ({VERSION_TYPE}) {VERSION_CODE}"

START_TIME = datetime.now()
SERVER_NAME = "QuartNG Server"
SERVER_NAME_SHORT = "QuartNG"
SERVER_ENGINE = "QNG"


INIT = False
template_path = os.path.join(os.path.dirname(__file__), "../static/templates")
JNINJA_ENV = Environment(loader=FileSystemLoader(template_path))


RATE_LIMIT = 20
RATE_LIMI_TIME_WINDOW = 20

PLUGINS = [
	"lib.plugins.home"
]