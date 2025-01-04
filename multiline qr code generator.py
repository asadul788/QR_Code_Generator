import qrcode
import os
from tkinter import Tk, Label, Text, Button, filedialog, messagebox

def generate_qr_code_from_gui():
    def save_qr_code():
        # Get the text from the input box
        text = text_input.get("1.0", "end-1c").strip()  # Get all text and remove trailing newline
        if not text:
            messagebox.showerror("Error", "Please enter some text to generate a QR code.")
            return
        
        # Ask user for the filename and destination
        filepath = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            title="Save QR Code As"
        )
        if not filepath:
            return  # User cancelled the save dialog
        
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

        messagebox.showinfo("Success", f"QR code saved as:\n{filepath}")

    # Create the main window
    root = Tk()
    root.title("QR Code Generator")

    # Create input label and text box
    Label(root, text="Enter text for the QR Code:").pack(pady=10)
    text_input = Text(root, width=40, height=10, wrap="word")
    text_input.pack(pady=10)

    # Create generate button
    Button(root, text="Generate and Save QR Code", command=save_qr_code).pack(pady=20)

    # Run the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    generate_qr_code_from_gui()

