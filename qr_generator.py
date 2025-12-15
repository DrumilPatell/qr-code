import qrcode
import os

url = input("Enter the URL to encode in QR code: ")

img = qrcode.make(url)

counter = 1
while os.path.exists(f"qrcode_{counter}.png"):
    counter += 1

filename = f"qrcode_{counter}.png"

img.save(filename)

print(f"QR code saved as {filename}")