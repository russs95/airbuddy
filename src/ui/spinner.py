import time

class Spinner:
    """
    Centered breathing-ring spinner for OLED.
    """

    def __init__(self, oled, interval=0.15):
        self.oled = oled
        self.interval = interval

        # Frames grow and shrink symmetrically
        self.frames = [
            "  ░░░░  ",
            " ░░░░░░ ",
            "░░░░░░░░",
            "████████",
            "░░░░░░░░",
            " ░░░░░░ ",
        ]

    def spin(self, duration=6, label="Reading air…"):
        end_time = time.time() + duration
        i = 0

        # Draw label once (top), spinner centered vertically
        while time.time() < end_time:
            frame = self.frames[i]

            self.oled.text([
                "",                # line 0 (padding)
                label.center(16),  # line 1
                "",                # line 2
                frame.center(16),  # line 3 (center)
            ])

            i = (i + 1) % len(self.frames)
            time.sleep(self.interval)
