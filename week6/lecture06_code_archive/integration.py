# Ref.: B. Slatkin, Effective Python: 125 Specific Ways to Write Better Python, 
# 3rd ed., Addison-Wesley Professional, 2024.

class Toaster:
    def __init__(self, timer):
        self.timer = timer
        self.level = 3
        self.hot = False

    def _get_duration(self):
        return max(0.1, min(120, self.level * 10))

    def push_down(self):
        if self.hot:
            return

        self.hot = True
        self.timer.countdown(self._get_duration(), self.pop_up)

    def pop_up(self):
        print("\nPop!")  # Release the spring
        self.hot = False
        self.timer.end()


import threading

class ReusableTimer:
    def __init__(self):
        self.timer = None

    def countdown(self, duration, callback):
        self.end()
        self.timer = threading.Timer(duration, callback)
        self.timer.start()

    def end(self):
        if self.timer:
            self.timer.cancel()
