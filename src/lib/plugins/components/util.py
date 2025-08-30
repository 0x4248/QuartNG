class time:
    def current(wrap_element="span", self_update=False) -> str:
            """ Returns the current time in a formatted string.
            """
            if self_update == False:
                from datetime import datetime
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                return f"<{wrap_element}>{now}</{wrap_element}>"
            else:
                import random
                id = random.randint(1000, 9999)
                return f"""
                <{wrap_element} id="{wrap_element}_{id}"></{wrap_element}>
                <script>
                    document.getElementById("{wrap_element}_{id}").innerHTML = new Date().toLocaleString();
                    setInterval(() => {{
                        document.getElementById("{wrap_element}_{id}").innerHTML = new Date().toLocaleString();
                    }}, 1000);
                </script>
                """
        