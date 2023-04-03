from typing import Callable, Any
import functools
import time

__all__ = ["DEBUG", "TIMER"]

class __Debug:
    def __init__(self) -> None:
        self.ON = False

    def PRINT(self, *args) -> None:
        if self.ON:
            print(*args)

DEBUG = __Debug()

def TIMER(REPEAT:int=10000):
    def decorator(func:Callable) -> Callable:
        OUTMOST = True
        @functools.wraps(func)
        def __wrapper(*args, **kwargs) -> Any:
            nonlocal OUTMOST
            result = None
            if OUTMOST:
                OUTMOST = False
                startTime = time.time_ns()
                for i in range(REPEAT):
                    result = func(*args, **kwargs)
                endTime = time.time_ns()
                runningTime = float(((endTime - startTime) / REPEAT) / (10 ** 9))
                print("Finish executing %s in %.3g s" % (func.__name__, runningTime))
                OUTMOST = True
            else:
                result = func(*args, **kwargs)
            return result
        return __wrapper
    return decorator

if __name__ == "__main__":
    pass