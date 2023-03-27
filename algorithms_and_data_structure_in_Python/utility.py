DEBUG = False

def DEBUG_PRINT(*arguments) -> None:
    if DEBUG:
        print(*arguments)