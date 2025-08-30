from lib.core import globals as GLOBAL
from lib.core import logger

def css_plugin_dep(name):
    # adds a CSS file to the CSS list and ignores if it is already on it
    if name not in GLOBAL.CSS:
        logger.log("css_plugin", f"Adding CSS dependency: {name}")
        GLOBAL.CSS.append(name)

def compile_css():
    logger.log("css_compile", "Compiling CSS")
    css_files = GLOBAL.CSS
    if not css_files:
        logger.log_warning("css_compile", "No CSS files found")
        return None

    compiled_css = []
    for file in css_files:
        file_path = f"src/lib/static/css/{file}.css"
        logger.log("css_compile", f"Compiling {file}.css")
        try:
            with open(file_path, "r") as css_file:
                compiled_css.append(css_file.read())
            logger.log("css_compile", f"Compiled {file}.css")
        except FileNotFoundError:
            logger.log_error("css_compile", f"File not found: {file_path}. Check config.json")
        except Exception as e:
            logger.log_error("css_compile", f"Error compiling {file}.css: {e}")

    return "\n".join(compiled_css) if compiled_css else None