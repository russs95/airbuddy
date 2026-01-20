import time

class Spinner:
    """
    Simple ASCII spinner for OLED.
    Call .next_frame() each time you want to draw the next frame.
    """
    def __init__(self, frames=None):
        self.frames = frames or ["|", "/", "-", "\\"]
        self.i = 0

    def next_frame(self) -> str:
        frame = self.frames[self.i]
        self.i = (self.i + 1) % len(self.frames)
        return frame

    def sleep(self, seconds: float = 0.1):
        time.sleep(seconds)
