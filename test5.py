# Bon bah ça renvoie un truc mais c'est pas incroyable

from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import requests
from PIL import Image

# import sys # to access the system
# import cv2

processor = TrOCRProcessor.from_pretrained("microsoft/trocr-base-handwritten")
model = VisionEncoderDecoderModel.from_pretrained("microsoft/trocr-base-handwritten")

# load image from the IAM dataset
url = "https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg"
image = Image.open("page_cahier.jpg").convert("RGB")
# image = Image.open(requests.get(url, stream=True).raw).convert("RGB")

pixel_values = processor(image, return_tensors="pt").pixel_values
generated_ids = model.generate(pixel_values)

generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

print("debut du texte")
print(generated_text)
print("fibn du texte")


image.show()
