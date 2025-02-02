import qrcode  # Import the qrcode library to generate QR codes
import os  # Import os for file operations
from PIL import Image  # Import Image from PIL for image manipulation

def split_text(text, max_length):
    """
    Splits the input text into chunks of the specified maximum length.
    
    Parameters:
    text (str): The input text to be split.
    max_length (int): The maximum length of each chunk.
    
    Returns:
    list: A list of text chunks.
    
    This function takes a long string of text and splits it into smaller chunks,
    each with a maximum specified length. This is useful for generating multiple
    QR codes when the input text is too long to fit into a single QR code.
    """
    # Split the text into chunks of max_length
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

def generate_qr_codes(data, base_filename, error_correction, box_size, border, fg_color, bg_color):
    """
    Generates QR codes from the given data and saves them as images.
    
    Parameters:
    data (str): The input data to encode in the QR codes.
    base_filename (str): The base filename for the saved QR code images.
    error_correction (str): The error correction level for the QR codes.
    box_size (int): The size of each box in the QR code.
    border (int): The size of the border around the QR code.
    fg_color (str): The foreground color of the QR code.
    bg_color (str): The background color of the QR code.
    
    Returns:
    list: A list of filenames for the generated QR code images.
    
    This function generates QR codes from the given data. It splits the data
    into chunks if it is too long to fit into a single QR code. Each QR code
    is customized with the specified error correction level, box size, border,
    and colors. The generated QR code images are saved with a unique filename,
    and the filenames are returned.
    """
    filenames = []  # List to store the filenames of the generated QR codes
    
    # Map error correction level to qrcode constants
    error_correction_map = {
        "Low": qrcode.constants.ERROR_CORRECT_L,
        "Medium": qrcode.constants.ERROR_CORRECT_M,
        "Quartile": qrcode.constants.ERROR_CORRECT_Q,
        "High": qrcode.constants.ERROR_CORRECT_H,
    }
    
    # Maximum characters based on version 40 and error correction level
    max_chars = {
        qrcode.constants.ERROR_CORRECT_L: 2953,
        qrcode.constants.ERROR_CORRECT_M: 2331,
        qrcode.constants.ERROR_CORRECT_Q: 1663,
        qrcode.constants.ERROR_CORRECT_H: 1273,
    }
    
    # Split the data into chunks based on the maximum characters allowed
    chunks = split_text(data, max_chars[error_correction_map[error_correction]])
    
    # Iterate over each chunk to generate a QR code
    for i, chunk in enumerate(chunks):
        # Create a QRCode object with the specified parameters
        qr = qrcode.QRCode(
            version=None,
            error_correction=error_correction_map[error_correction],
            box_size=box_size,
            border=border,
        )
        
        # Add the chunk of data to the QR code
        qr.add_data(chunk)
        qr.make(fit=True)  # Adjust the QR code to fit the data
        
        # Generate the QR code image with the specified foreground and background colors
        img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert("RGB")
        
        # Generate a unique filename for the QR code image
        filename = f"{base_filename}_{i+1}.png"
        
        # Save the QR code image to the specified filename
        img.save(filename)
        
        # Add the filename to the list of filenames
        filenames.append(filename)
    
    # Return the list of filenames for the generated QR codes
    return filenames