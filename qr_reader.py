from pyzbar.pyzbar import decode  # Import decode from pyzbar for QR code decoding
from PIL import Image  # Import Image from PIL for image manipulation

def read_multiple_qr_codes(paths):
    """
    Reads and decodes QR codes from multiple image files.
    
    Parameters:
    paths (list): A list of file paths to the QR code images.
    
    Returns:
    str: The decoded data from the QR codes.
    
    This function takes a list of file paths to QR code images and reads
    the QR codes from each image. It decodes the QR codes and concatenates
    the decoded data into a single string. This is useful for processing
    multiple QR codes in a batch.
    """
    decoded_data = []  # List to store the decoded data from each QR code
    
    # Iterate over each file path
    for path in paths:
        try:
            # Open the image file
            img = Image.open(path)
            
            # Decode the QR code from the image
            decoded_objects = decode(img)
            
            if not decoded_objects:
                print(f"No QR code found in file: {path}")
                continue
            
            # Extract the decoded data and add it to the list
            for obj in decoded_objects:
                decoded_data.append(obj.data.decode('utf-8'))
        
        except Exception as e:
            print(f"Error decoding QR code from file {path}: {e}")
    
    # Concatenate the decoded data into a single string
    return '\n'.join(decoded_data)

def read_large_qr_code_image(path):
    """
    Reads and decodes a QR code from a large image file by splitting it into smaller sections.
    
    Parameters:
    path (str): The file path to the large QR code image.
    
    Returns:
    str: The decoded data from the QR code.
    
    This function reads a large QR code image by splitting it into smaller sections
    and then decoding each section. The decoded data is concatenated and returned.
    """
    decoded_data = []
    
    try:
        # Open the large image file
        img = Image.open(path)
        width, height = img.size
        
        # Define the size of each section
        section_size = 1000  # Adjust this value based on the size of your QR codes
        
        # Split the image into smaller sections
        for i in range(0, width, section_size):
            for j in range(0, height, section_size):
                box = (i, j, i + section_size, j + section_size)
                section = img.crop(box)
                
                # Decode the QR code from the section
                decoded_objects = decode(section)
                
                # Extract the decoded data and add it to the list
                for obj in decoded_objects:
                    decoded_data.append(obj.data.decode('utf-8'))
    
    except Exception as e:
        print(f"Error decoding large QR code from file {path}: {e}")
    
    # Concatenate the decoded data into a single string
    return '\n'.join(decoded_data)