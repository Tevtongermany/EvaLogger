ANSI = "\033["


def color(code):
    return ANSI + str(code) + "m"


class Colors:
    BLACK = color(30)
    RED = color(31)
    GREEN = color(32)
    YELLOW = color(33)
    BLUE = color(34)
    TURKIS = color(36)
    MAGENTA = color(35)
    RESET = color(0)
