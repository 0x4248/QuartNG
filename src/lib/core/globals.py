import subprocess
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
import os
import json


with open("src/config.json") as f:
    data = json.load(f)
    PLUGINS = data.get("plugins", [])
    CSS = data.get("css", [])

NAME = "QuartNG"
AUTHOR = "0x4248"
DESCRIPTION = "This is the default description for QuartNG, you can change it in globals.py"

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
