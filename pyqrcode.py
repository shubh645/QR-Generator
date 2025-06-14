import qrcode # type: ignore

# Data to be encoded
data = input(str("ENTER THE LINK "))

# Creating an instance of QRCode class
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in pixels
    border=4,  # Border size in boxes
)

# Adding data to the instance
qr.add_data(data)
qr.make(fit=True)

# Creating an image from the QRcode instance
img = qr.make_image(fill_color="black", back_color="orange")

# Saving the image
img.save("qrcode.png")

# Display the image (optional)
img.show()
