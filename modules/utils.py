from re       import sub
from pytermx  import Color
from datetime import datetime

class Print:
    @staticmethod
    def _message(typee, text):
        try:
            text = sub(r'\[(.*?)]', rf"{Color.GREY}[{Color.BRIGHT_WHITE}\1{Color.GREY}]{Color.BRIGHT_WHITE}", text)
        except:
            pass

        return f"{Color.BLACK}{datetime.now().strftime('%H:%M:%S')} {typee} {Color.BRIGHT_WHITE} {text}"

    @staticmethod
    def inf(text: str):
        print(Print._message(f"{Color.BLUE}INF", text))

    @staticmethod
    def success(text: str):
        print(Print._message(f"{Color.GREEN}YES", text))

    @staticmethod
    def error(text: str):
        print(Print._message(f"{Color.RED}ERR", text))

    @staticmethod
    def debug(text: str):
        print(Print._message(f"{Color.YELLOW}DBG", text))

    @staticmethod
    def ask(text: str):
        return Print._message(f"{Color.PURPLE}INP", text)
    
    @staticmethod
    def vert(text: str, **kwargs):
        first_message = Print._message(f"{Color.GREEN}INF", f"{Color.BLUE}{text}{Color.BRIGHT_WHITE}")

        for index, (key, value) in enumerate(kwargs.items()):
            prefix = "\t ├" if index < len(kwargs) - 1 else "\t └"
            line = f"{prefix} {Color.BRIGHT_WHITE}{key}: {value}"

            first_message += f"\n{line}"

        print(first_message)