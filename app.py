import qrcode

def generate_qr_code(link, filename, color='black'):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color="white")
    img.save(f'generated/{filename}')

if __name__ == "__main__":

    link = input("Enter the link: ")
    filename = input("Enter the filename (with extension) to save QR code: ")
    color = input("Enter the color(optional): ")
    
    generate_qr_code(link, filename, color)
    print(f"QR code saved as {filename}")
