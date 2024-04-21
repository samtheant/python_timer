from timer import Timer, timer
import time
import random

@Timer("testFunctionDecorator")()
def testFunctionDecorator(seconds: float):
    time.sleep(seconds)

def testFunction(seconds: float):
    timer["testFunction"].start()
    time.sleep(seconds)
    timer["testFunction"].stop()


if __name__ == "__main__":
    for i in range(10):
        num = random.random()
        testFunctionDecorator(num)
        testFunction(num)
    Timer.timers["testFunctionDecorator"].print_summary()
    Timer.timers["testFunction"].print_summary()