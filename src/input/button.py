# src/input/button.py
import time
from gpiozero import Button


class AirBuddyButton:
    def __init__(self, gpio_pin=17, click_window_s=1.0):
        """
        click_window_s:
            Total time window after first press to collect extra clicks.
            Example: 1.0 means:
              - after the first click, we wait up to 1 second for 2nd/3rd clicks
        """
        self.button = Button(gpio_pin, pull_up=True, bounce_time=0.05)
        self.click_window_s = float(click_window_s)

    def wait_for_action(self):
        """
        Blocking call.

        Returns:
            "single", "double", or "triple"

        Behavior:
            - Wait for first press (blocking)
            - Then open a window (click_window_s) to capture additional presses
            - Count press *events* (edges), not "is_pressed" level
        """
        # --- First click (blocking) ---
        self.button.wait_for_press()
        self.button.wait_for_release()
        click_count = 1

        start = time.monotonic()

        # --- Collect 2nd/3rd clicks within the window ---
        while click_count < 3:
            remaining = self.click_window_s - (time.monotonic() - start)
            if remaining <= 0:
                break

            # Wait for the next press event (edge) within the remaining time
            pressed = self.button.wait_for_press(timeout=remaining)
            if not pressed:
                break  # window expired, no more clicks

            # Count it, then wait for release to avoid counting a hold as extra clicks
            self.button.wait_for_release()
            click_count += 1

        if click_count == 1:
            return "single"
        if click_count == 2:
            return "double"
        return "triple"
