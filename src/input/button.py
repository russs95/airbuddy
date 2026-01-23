# src/input/button.py
import time
from gpiozero import Button


class AirBuddyButton:
    def __init__(self, gpio_pin=17, click_window_s=1.0):
        """
        click_window_s:
            Total time window after first press to collect
            additional clicks (2nd, 3rd).
        """
        self.button = Button(gpio_pin, pull_up=True, bounce_time=0.05)
        self.click_window_s = float(click_window_s)

    def wait_for_action(self):
        """
        Blocking call.

        Returns:
            "single"
            "double"
            "triple"

        Behavior:
            - Wait for first press
            - Open a 1s window
            - Count how many presses occur
        """
        click_count = 0

        # --- First press (blocking) ---
        self.button.wait_for_press()
        self.button.wait_for_release()
        click_count = 1

        start = time.monotonic()

        # --- Collect additional presses ---
        while (time.monotonic() - start) < self.click_window_s:
            if self.button.is_pressed:
                self.button.wait_for_release()
                click_count += 1

                # Cap at 3 (we don't care beyond triple)
                if click_count >= 3:
                    return "triple"

            time.sleep(0.01)

        # --- Decide action ---
        if click_count == 1:
            return "single"
        elif click_count == 2:
            return "double"
        else:
            return "triple"
