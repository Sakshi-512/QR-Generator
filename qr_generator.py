import qrcode

img = qrcode.make("https://wa.me/9*********")
img.save("whatsapp_qr.png")
