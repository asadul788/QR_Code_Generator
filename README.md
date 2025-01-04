# QR_Code_Generator
This is a QR Code Generation Python Script


Here’s a README file that explains the purpose and usage of the two files:

---

# QR Code Generators

This repository contains two Python scripts for generating QR codes. Both scripts allow users to create QR codes from input text and save them as PNG images. The scripts differ in their user interface and functionality.

## Files

### 1. `qr_code_generator.py`
This script generates a QR code using a command-line interface.

- **Features**:
  - Prompts the user to enter the text for the QR code.
  - Allows specifying a filename for saving the QR code.
  - You Can change your save directory "destination_folder = r"D:\\QR Code Generator""
    here you have to replace the 'D:\\QR Code Generator' to your destination path.

- **How to Use**:
  1. Run the script: `python qr_code_generator.py`
  2. Follow the prompts to input the text and filename.
  3. The QR code will be saved as a PNG file in the specified directory.

---

### 2. `multiline_qr_code_generator.py`
This script provides a GUI-based approach for QR code generation.

- **Features**:
  - Simple graphical interface built with `tkinter`.
  - Allows users to enter multiline text for the QR code.
  - Provides a file dialog to choose the save location and filename.

- **How to Use**:
  1. Run the script: `python multiline_qr_code_generator.py`
  2. Enter the desired text into the text box.
  3. Click the "Generate and Save QR Code" button.
  4. Choose the save location and filename using the file dialog.
  5. The QR code will be saved as a PNG file at the selected location.

---

## Requirements

Both scripts require the `qrcode` library and other built-in modules (`os`, `tkinter`, etc.).

### Installation
To install the required library, run:
```bash
pip install qrcode[pil]
```

---

## Use Cases
- `qr_code_generator.py`: Ideal for users comfortable with command-line tools who need a straightforward way to generate QR codes.
- `multiline_qr_code_generator.py`: Suitable for users who prefer a graphical interface and need to handle multiline text.

---

Feel free to modify the scripts to suit your specific requirements!
