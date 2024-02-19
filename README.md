# AmPiLight client
### This program was made as final project for CS50x course
Video showcase is available under [this link](https://youtu.be/XjO_DUD1B1E).

### Description
This is a linux client for AmPiLight.

AmPiLight is a program that aims to do effect like Philips Ambilight, but using RaspberryPi as NeoPixel LED controller.

This program works like that:
- Gets screenshot.
- Divides screenshot to few areas near the monitor borders.
- Checks color medians of each area.
- Connects to server using integrated to python module for networking called **socket**.
- Pickles data to make it able to sand via network.
- Sends pickled data.

The next part is server's job, but I will describe it here:
- Receives data.
- Depickles data.
- Sends data to ARGB strp using **NeoPixel** module.

Note that sometimes bad data may be sent and latency may vary depending on your network installation.

After installation it is necessary to change your configuration from both server and client side in `config.json` files.

To exit program simply press Ctrl+C in terminal. If program is terminated from one side, second side automatically terminates also.

## Hardware requirements
You will need to prepare **Raspberry Pi** and **NeoPixel ARGB strip**.

You should mount the LED strip behind your monitor (diodes amount may vary depending on your monitor size, density of diodes on the strip).

Once you got all the hardware you have to connect connect the strip to the RaspberryPi. Of course you can use external power source (it would be even better if you will), but the most important is to connect the **Din** line to RaspberryPi's **GPIO**.

You can some find examples of wiring [HERE](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring).

## Installation, configuration and running
**Note that you will also need a [server side](https://github.com/Zabbum/AmPiLight-server) to make program work.**

### Installation
1. Clone the repository and navigate to it.
```
git clone https://github.com/Zabbum/AmPiLight-client.git
cd AmPiLight-client
```
2. Install required dependencies.
```
sudo pip3 install screeninfo pillow
```
### Configuration
`config.json` contains all the configuration.
- `serverAddress` is address of AmPiLight server.
- `"serverPort"` is what port does the AmPiLight server use
- `"LEDAmount"`
    - `"vertical"` is how many diodes are vertically behind monitor. [ex. `10`]
    - `"horizontal"` is how many diodes are horizontally behind monitor. [ex. `16`]

### Running
You simply run the `app.py`.
```
python3 app.py
```