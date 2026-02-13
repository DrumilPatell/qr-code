import qrcode
import os
from PIL.Image import Image as PILImage

url = input("Enter the URL to encode in QR code: ")

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img: PILImage = qr.make_image(fill_color="black", back_color="white")  # type: ignore

counter = 1
while os.path.exists(f"qrcode_{counter}.png"):
    counter += 1

filename = f"qrcode_{counter}.png"

img.save(filename)  # type: ignore

print(f"QR code saved as {filename}")