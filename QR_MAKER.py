import qrcode
img=qrcode.make("https://codingblockslpu.vercel.app/participate")
img.save("myqr.png")