import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306


class OLED:
    """
    SSD1306 OLED helper with:
    - Google Fonts support (Arvo for title, Mulish for UI)
    - pixel-accurate centering
    - stable redraws (no undefined variables)
    """

    def __init__(self, width=128, height=64, addr=0x3C):
        # I2C init
        i2c = busio.I2C(board.SCL, board.SDA)
        self.oled = adafruit_ssd1306.SSD1306_I2C(width, height, i2c, addr=addr)

        self.width = width
        self.height = height

        # Persistent buffer
        self.image = Image.new("1", (self.width, self.height))
        self.draw = ImageDraw.Draw(self.image)

        # Fonts (safe fallback if missing)
        try:
            self.font_title = ImageFont.truetype(
                "assets/fonts/Arvo-Regular.ttf", 22
            )
            self.font_small = ImageFont.truetype(
                "assets/fonts/Mulish-Regular.ttf", 10
            )
            self.font_large = ImageFont.truetype(
                "assets/fonts/Mulish-Regular.ttf", 22
            )
        except Exception:
            self.font_title = ImageFont.load_default()
            self.font_small = ImageFont.load_default()
            self.font_large = ImageFont.load_default()

        self.oled.fill(0)
        self.oled.show()

    # ---------- helpers ----------

    def clear(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.oled.image(self.image)
        self.oled.show()

    def _center_x(self, text, font):
        bbox = self.draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        return max(0, (self.width - text_w) // 2)

    def draw_centered(self, text, y, font):
        x = self._center_x(text, font)
        self.draw.text((x, y), text, font=font, fill=255)

    # ---------- screens ----------

    def show_waiting(self, line="Waiting for button"):
        """
        Idle screen — no spinner logic here.
        """
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        self.draw_centered("airBuddy", 10, self.font_title)
        self.draw_centered(line, 34, self.font_small)

        self.oled.image(self.image)
        self.oled.show()

    def show_spinner_frame(self, label, spinner_text):
        """
        Spinner-only frame (no label text).
        """
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        spinner_y = (self.height // 2) - 12
        self.draw_centered(spinner_text, spinner_y, self.font_large)

        self.oled.image(self.image)
        self.oled.show()

    def show_results(self, temp_c, eco2_ppm, tvoc_ppb, rating="GOOD"):
        """
        Data-only results screen.
        """
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

        y = 6
        self.draw.text((2, y), f"Temp: {temp_c:>4.1f} C", font=self.font_small, fill=255)
        self.draw.text((2, y + 16), f"eCO2: {eco2_ppm:>4d} ppm", font=self.font_small, fill=255)
        self.draw.text((2, y + 32), f"TVOC: {tvoc_ppb:>4d} ppb", font=self.font_small, fill=255)

        self.draw_centered(f"AIR: {rating}", 50, self.font_small)

        self.oled.image(self.image)
        self.oled.show()
