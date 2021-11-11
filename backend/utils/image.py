import base64
from typing_extensions import Required
from PIL import Image, ImageColor
from os import path
import requests


def saveImage(base64Image, fileName):

    """
    save the image to the static folder
    """
    img = Image.open(base64.b64decode(base64Image))
    img.save(path.join("static", "images", f"{fileName}.png"), "PNG")


def getImage(fileName):
    """
    grabs the image from the static folder, or a internet link and returns it as a base64 string
    """

    if path.isfile(fileName):
        with open(path.join("static", "images", fileName), "rb") as imageFile:
            return base64.b64encode(imageFile.read())

    response = requests.get(url=fileName)
    if response.ok:
        return base64.b64encode(response.content)

    print("given file not found")
    return base64.b64encode(Image.new("RGB", [100, 100], ImageColor.getcolor("red")))