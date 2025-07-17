def h(level: int, content: str) -> str:
    return f"<h{level}>{content}</h{level}>"

def span(content: str, class_name: str = "") -> str:
    class_attr = f' class="{class_name}"' if class_name else ""
    return f"<span{class_attr}>{content}</span>"

def p(content: str, class_name: str = "") -> str:
    class_attr = f' class="{class_name}"' if class_name else ""
    return f"<p{class_attr}>{content}</p>"

def strong(content: str, class_name: str = "", id: str = "") -> str:
    class_attr = f' class="{class_name}"' if class_name else ""
    id_attr = f' id="{id}"' if id else ""
    return f"<strong{class_attr}{id_attr}>{content}</strong>"

def hr() -> str:
    return "<hr>"