# AmPiLight client
### Description
AmPiLight is a program that aims to do effect like Philips Ambilight, but using RaspberryPi as NeoPixel LED controller.

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
### Running
You simply run the `app.py`.
```
python3 app.py
```