from clarifai.rest import ClarifaiApp
from PIL import Image
import requests
from io import BytesIO

app = ClarifaiApp("t_PWeUfWygWotDHWGPW6llqt2-nxMMTDNdNK1n39", "bDSBvO-qsHqRUcmNwGGCcxgJMr6eursYE4TgnZtb")

#response = requests.get("https://samples.clarifai.com/demographics.jpg")
#img = BytesIO(response.content)

img = Image.Open("C:\\Users\mr0028\Desktop\demographics-001.jpg")

model = app.models.get('demographics')

model.predict([img])
