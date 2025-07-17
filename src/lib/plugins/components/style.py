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

class Link:
    def text_decor(link: str, text: str, decoration_l: str = "[", decoration_r: str = "]") -> str:
        return f"{decoration_l}<a href='{link}'>{text}</a>{decoration_r}"