import qrcode

user_input = input('Enter your text or URL: ').strip()
filename = input('Enter your desired filename (e.g., myqr.png): ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(user_input)
qr.make(fit=True)

image = qr.make_image(fill_color='black', back_color='white')
image.save(filename)

print(f'QR code saved as {filename}')
