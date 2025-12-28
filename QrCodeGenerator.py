from qrcode import QRCode

qr = QRCode(
    version = 1,
    box_size = 10,
    border = 5,
    
)

directory = input("Enter your location: ")
qr.add_data(directory)
qr.make(fit=True)

img = qr.make_image(fill_color="white", back_color="pink")
img.save("Code.png")
print("Done")