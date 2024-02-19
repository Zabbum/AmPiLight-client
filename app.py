# Import modules
from helpers import RGBmedians
import json
from screeninfo import get_monitors
import socket, pickle

# Global variables
monitorHeight = get_monitors()[0].height
monitorWidth = get_monitors()[0].width
serverAddress = 0
serverPort = 0
pxAmount = 0

# Get configuration from file
with open("config.json") as configFile:
    jsonData = json.load(configFile)
    serverAddress = jsonData["serverAddress"]
    serverPort = jsonData["serverPort"]
    pxAmount = configFile["LEDAmount"]

pixelAverageHeight = int(monitorHeight / pxAmount['vertical'])
pixelAverageWidth = int(monitorWidth / pxAmount['horizontal'])

# Network setup
print("Initializing network setup...")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    clientSocket.connect((serverAddress, serverPort))
except ConnectionRefusedError:
    print("Connection refused.")
    exit(1)

# Program loop
print("Connected!")
try:
    while True:
        try:
            RGBdata = RGBmedians( # Get the RGB data
                pxAmount['horizontal'], pxAmount['vertical'],
                pixelAverageWidth, pixelAverageHeight
            )
            print(RGBdata) # Log the data
            serializedData = pickle.dumps(RGBdata) # Serialize data
            clientSocket.sendall(serializedData) # Send data
        except BrokenPipeError as error:
            print(f"Error: {error}. Continuing.")
            continue

# If received terminate signal, end program casually.
except KeyboardInterrupt:
    # Close the connection
    clientSocket.close()
    exit()

# If server closes program, close program
except ConnectionResetError:
    print("Connection closed.")
    clientSocket.close()
    exit(1)
