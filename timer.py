import time
import functools

class Timer():
    timers = {}
    def __init__(self, name: str):
        self.num_calls = 0
        self.total_time = 0
        self.function_name = name
        self.started = False
        Timer.timers[name] = self

    def __call__(self):
        def decorator_time_function(func):
            @functools.wraps(func)
            def time_wrapper(*args, **kwargs):
                start = time.perf_counter()
                return_val = func(*args, **kwargs)
                end = time.perf_counter()
                self.num_calls += 1
                self.total_time += end - start
                return return_val
            return time_wrapper
        return decorator_time_function

    def __getitem__(self, key):
        if key in self.timers.keys():
            return self.timers[key]
        else:
            new_timer = Timer(key)
            self.timers[key] = new_timer
            return new_timer
    
    def print_summary(self):
        if self.num_calls > 0:
            print(f"{self.function_name : <50} total = {self.total_time:8.4f} secs        average = {self.total_time / self.num_calls:8.4f} called {self.num_calls} times")
            # print(f"Average time: {self.total_time / self.num_calls:0.4f}")
        else:
            print(f"{self.function_name} has not been called")

    def start(self):
        self.start_time = time.perf_counter()
        self.started = True

    def stop(self):
        if self.started:
            self.stop_time = time.perf_counter()
            self.total_time += self.stop_time - self.start_time
            self.num_calls += 1
            self.started = False

timer = Timer("dummy timer")