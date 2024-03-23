# Import modules
from PIL import Image, ImageDraw, ImageGrab, ImageStat

def RGBmedians(pixelWidth: int, pixelHeight: int, pixelAverageWidth: int, pixelAverageHeight: int):
    screenshot = ImageGrab.grab()       # Screenshot
    pixels = []                         # List with all pixels values (RGB)

    # Left side
    for pixel in range(pixelHeight):
        # Create full black mask
        mask = Image.new("L", screenshot.size)
        # Select mask to draw
        draw = ImageDraw.Draw(mask)
        # Create mask with specific region masked
        draw.rectangle([0,                      screenshot.height - (pixel + 1) * pixelAverageHeight,
                        pixelAverageWidth - 1,  screenshot.height - pixel * pixelAverageHeight],
                        fill=255)
        # Get median of color for region
        median = ImageStat.Stat(screenshot, mask=mask).median
        # Add median to the list
        pixels.append(median)
    
    # Top side
    for pixel in range(pixelWidth):
        # Create full black mask
        mask = Image.new("L", screenshot.size)
        # Select mask to draw
        draw = ImageDraw.Draw(mask)
        # Create mask with specific region masked
        draw.rectangle([pixel * pixelAverageWidth,          0,
                        (pixel + 1) * pixelAverageWidth,    pixelAverageHeight],
                        fill=255)
        # Get median of color for region
        median = ImageStat.Stat(screenshot, mask=mask).median
        # Add median to the list
        pixels.append(median)
    
    # Right side
    for pixel in range(pixelHeight):
        # Create full black mask
        mask = Image.new("L", screenshot.size)
        # Select mask to draw
        draw = ImageDraw.Draw(mask)
        # Create mask with specific region masked
        draw.rectangle([screenshot.width - pixelAverageWidth,   pixel * pixelAverageHeight,
                        screenshot.width,                       (pixel + 1) * pixelAverageHeight],
                        fill=255)
        # Get median of color for region
        median = ImageStat.Stat(screenshot, mask=mask).median
        # Add median to the list
        pixels.append(median)

    return pixels
