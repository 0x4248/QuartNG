from lib.core.page import compile

def center_text(components: list, class_name: str = "") -> str:
    ret = (
        f'<div style="text-align: center;" class="{class_name}">'
        f'{compile(components)}'
        '</div>'
    )
    return ret


def half_split(left: list, right: list, class_name: str = "") -> str:
    """
    Splits the screen into two halves with left and right content.
    """

    return f"""
    <div class="{class_name}">
        <div style="float: left; width: 50%;">{compile(left)}</div>
        <div style="float: right; width: 50%;">{compile(right)}</div>
    </div>
    """


def wrap_class(class_name: str, content: list) -> str:
    """
    Wraps content with a class using a <div> class. Lets say you have a CSS class called
    center-text and want to set it for a specific chunk of content.
    """
    return f'<div class="{class_name}">{compile(content)}</div>'

def stick(content: list, position: str = "bottom", with_to_100: bool = True, class_name: str = "") -> str:
    """
    Sticks content to a specific position on the screen.
    """
    if with_to_100:
        return f'<div style="position: fixed; {position}: 0; width: 100%;">{compile(content)}</div>'
    return f'<div style="position: fixed; {position}: 0;">{compile(content)}</div>'


class link:
    def text_decor(link: str, text: str, decoration_l: str = "[", decoration_r: str = "]") -> str:
        """
        Makes a link have text decorations
        """
        return f"{decoration_l}<a href='{link}'>{text}</a>{decoration_r}"