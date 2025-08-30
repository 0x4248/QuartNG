from lib.core.page import compile
from lib.core.css import css_plugin_dep

def row_container(elements: list) -> str:
    css_plugin_dep("components/btn_grids")
    return f'<div class="btn_row_container">{compile(elements)}</div>'

def row_container_center(elements: list) -> str:
    css_plugin_dep("components/btn_grids")
    return f'<div class="btn_row_container_center">{compile(elements)}</div>'



def button_element(label: str) -> str:
    css_plugin_dep("components/btn_grids")
    return f'<button class="grid_btn">{label}</button>'