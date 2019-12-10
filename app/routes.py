from app import app
from PIL import Image
from flask import request, send_file
import io
import requests

nasa_api_key="NLrGq98UqsydqrbBJTkLnycjmrnR7ooDtgAlhZHk"
@app.route("/")
def get_image():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key={}".format(nasa_api_key)).json()
    image_response = requests.get(response["url"])
    imageBytes = image_response.content
    image = Image.open(io.BytesIO(imageBytes))
    image.save("NASA_Image_Of_The_Day.png")

    return send_file("../NASA_Image_Of_The_Day.png")