
import qrcode

def generate_qr_code():
    import os

    # Ask the user for input text
    text = input("Enter the text you want to convert into a QR code: ")
    
    # Ask the user for the filename (without extension)
    filename = input("Enter the filename to save the QR code: ")
    
    # Add .png extension and set destination folder
    destination_folder = r"D:\\QR Code Generator"
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    filepath = os.path.join(destination_folder, f"{filename}.png")
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    print(f"QR code generated and saved as {filepath}")

if __name__ == "__main__":
    generate_qr_code()