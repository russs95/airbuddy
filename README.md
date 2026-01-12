🌬️ airBuddy

Open‑source air quality testing for community health & climate justice
🌍 1. Overview

airBuddy is a small, open‑source air quality testing device built on a Raspberry Pi Zero 2 W.
It empowers individuals, schools, neighborhoods, and communities to measure the air they breathe and take ownership of their environmental health through knowledge, transparency, and data.

With one press of a button, airBuddy:

    Measures temperature & humidity

    Reads eCO₂ (equivalent CO₂) and TVOC (total volatile organic compounds)

    Estimates overall air quality

    Displays the results on a compact OLED screen

    Logs readings to a local data file for long‑term tracking

The goal is simple:

    If people can measure their air, they can demand better air.

airBuddy is designed to be:

    Affordable

    Hackable

    Community‑deployable

    Fully open source

🧩 2. Hardware Components
Component	Description
🧠 Raspberry Pi Zero 2 W	Core computer
💾 MicroSD Card (≥8GB)	Raspberry Pi OS Lite (Bookworm)
🔋 5V Power Source	USB power bank or regulated 5V
🌫 ENS160 + AHT21 Sensor Board	Measures eCO₂, TVOC, temperature & humidity
🖥 0.96" SSD1306 OLED (I²C)	128×64 pixel display
🔘 Momentary Push Button	Triggers an air quality test
🔌 Jumper Wires	Male–female & male–male
🪛 Breadboard (optional)	For prototyping
🌬️ 3. What airBuddy Does

When powered on, airBuddy shows an idle screen:

    “airBuddy — Press Button”

When the button is pressed:

    An ASCII spinner appears while readings are gathered

    The sensors collect:

        Temperature (°C)

        Humidity (%)

        eCO₂ (ppm equivalent)

        TVOC (ppb)

    A simple air‑quality rating is calculated

    Results are displayed for 10 seconds

    The readings are logged to /data/

    The device returns to idle mode

🧠 4. Raspberry Pi Zero 2 W GPIO Map

(SD Card Up, Power LED Down)

This table shows exactly how airBuddy connects to the Pi.
🧩 Pin Assignments
Pin	Signal	Connected To
🟥 1	3.3V	OLED VCC, Sensor VCC
🟨 3	GPIO2 (SDA)	OLED SDA, ENS160 SDA
🟩 5	GPIO3 (SCL)	OLED SCL, ENS160 SCL
⬛ 6	GND	OLED GND, Sensor GND
⬜ 11	GPIO17	Push Button (signal)
⬛ 14	GND	Push Button (ground)
🖥 OLED + Sensor Wiring (I²C Bus)

The OLED display and the ENS160/AHT21 sensor board share the same I²C bus.
OLED / Sensor Pin	Raspberry Pi
VCC	3.3V (Pin 1)
GND	GND (Pin 6)
SDA	GPIO2 / SDA (Pin 3)
SCL	GPIO3 / SCL (Pin 5)

Both devices can coexist on I²C because they use different addresses.
🔘 Push Button Wiring

The button uses the Pi’s internal pull‑up resistor.
Button Leg	Raspberry Pi
Leg 1	GPIO17 (Pin 11)
Leg 2	GND (Pin 14)

When pressed, the GPIO reads LOW.
🎨 Wiring Color Legend
Symbol	Color	Purpose
🟥	Red	3.3V Power
⬛	Black	Ground (GND)
🟨	Yellow	I²C Data (SDA)
🟩	Green	I²C Clock (SCL)
⬜	White	Button signal
⚪	—	Unused GPIO
🌱 Why airBuddy Matters

Air pollution is one of the largest hidden public‑health crises on Earth.
Yet most people cannot measure the air in their homes, schools, or neighborhoods.

airBuddy is about democratizing environmental data.

By making air quality measurable, visible, and shareable:

    Communities can identify problems

    Activists can collect evidence

    Families can protect their health

    Cities can be held accountable

Clean air should not be a luxury.
