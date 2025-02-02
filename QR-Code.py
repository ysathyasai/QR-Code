import streamlit as st
import pyperclip  # Clipboard functionality
from qr_generator import generate_qr_codes
import os
from datetime import datetime

# Function of the program:
# This Streamlit application allows users to generate, read, and scan QR codes.
# Users can generate custom QR codes with different data types and colors,
# read QR codes from uploaded images, and scan QR codes in real-time using their webcam.

# Set page config
st.set_page_config(
    page_title="QR Code Generator and Reader",  # Set the page title
    page_icon=":qrcode:",  # Set the page icon
    layout="centered",  # Set the layout to centered
    initial_sidebar_state="expanded"  # Set the initial sidebar state to expanded
)

# Custom CSS for UI Enhancements
hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}  /* Ensure the main menu is visible */
            footer {visibility: hidden;}  /* Hide the footer */
            header {visibility: hidden;}  /* Hide the header */
            .css-1v0mbdj {visibility: hidden;}  /* Hide the 'Deploy' button */
            .reportview-container {
                background-color: #f0f2f6;  /* Set a light background color */
            }
            .stButton>button {
                background-color: #2874A6;  /* Set button color */
                color: white;  /* Set button text color */
            }
            .stTextInput>div>input {
                border: 2px solid #2874A6;  /* Set input border color */
                border-radius: 8px;
            }
            .stTextArea>div>textarea {
                border: 2px solid #2874A6;  /* Set textarea border color */
                border-radius: 8px;
            }
            .stColorPicker>div>input {
                border: 2px solid #2874A6;  /* Set color picker border color */
                border-radius: 8px;
            }
            .stFileUploader>div>div>div>input {
                border: 2px solid #2874A6;  /* Set file uploader border color */
                border-radius: 8px;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  # Apply the custom CSS

# Title and Sidebar Menu
st.title("QR Code Generator and Reader")  # Set the main title of the app
st.sidebar.title("☰ Menu")  # Set the sidebar title
menu = ["Generate QR Code", "Read QR Code", "Scan QR Code"]  # Menu options
choice = st.sidebar.radio("Choose an option", menu, key="main_menu")  # Sidebar radio buttons for menu options

# QR Code Generation
if choice == "Generate QR Code":
    st.header("Generate QR Code")  # Set the header for QR Code generation
    st.markdown("### Create custom QR codes with different data types and colors.")  # Description for QR Code generation
    
    col1, col2 = st.columns(2)  # Create two columns for input fields
    with col1:
        data_type = st.selectbox("Select Data Type", ["Text", "URL", "Batch"])  # Dropdown to select data type
    with col2:
        error_correction = st.selectbox("Error Correction Level", ["Low", "Medium", "Quartile", "High"])  # Dropdown to select error correction level
    
    col3, col4 = st.columns(2)  # Create two more columns for input fields
    with col3:
        box_size = st.slider("Box Size", 1, 20, 10)  # Slider to select box size
    with col4:
        border = st.slider("Border Size", 1, 10, 4)  # Slider to select border size
    
    fg_color = st.color_picker("Foreground Color", "#000000")  # Color picker for foreground color
    bg_color = st.color_picker("Background Color", "#FFFFFF")  # Color picker for background color
    
    with st.form(key='qr_form'):
        data = st.text_area("Enter data to encode", height=200, key="qr_data")  # Text area to input data
        submit_button = st.form_submit_button(label='Generate')  # Submit button to generate QR Code
    
    if submit_button:
        if data.strip():  # Check if data is not empty
            # Generate a unique filename based on the current date and time
            filename = os.path.join('saved_qr', datetime.now().strftime("%d%m%Y-%H%M%S"))
            # Generate QR codes with the specified parameters
            filenames = generate_qr_codes(data, filename, error_correction, box_size, border, fg_color, bg_color)
            
            st.markdown("### Generated QR Codes")  # Display the generated QR codes
            # Iterate over the filenames and display each generated QR code
            for file in filenames:
                st.image(file, caption=f"Generated QR ({os.path.basename(file)})", use_container_width=True)  # Display the QR code image
                # Provide a download button for each QR code image
                with open(file, "rb") as img_file:
                    st.download_button("Download QR Code", img_file, file_name=f"{os.path.basename(file)}")
        else:
            st.error("Please enter data to encode")  # Display an error message if data is empty

    # Display last 10 generated QR codes
    st.subheader("Recent QR Codes")  # Subheader for recent QR codes
    if os.path.exists('saved_qr'):
        # Get the last 10 generated QR codes and display them
        saved_qrs = sorted(os.listdir('saved_qr'), reverse=True)[:10]
        for qr in saved_qrs:
            st.image(os.path.join('saved_qr', qr), caption=qr)  # Display each QR code

# QR Code Reading
elif choice == "Read QR Code":
    st.header("Read QR Code")  # Set the header for QR Code reading
    st.markdown("### Upload QR code images to decode their content.")  # Description for QR Code reading
    # File uploader to upload QR code images
    uploaded_files = st.file_uploader("Upload QR Code Image(s)", type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if uploaded_files:
        saved_paths = []  # List to store the paths of uploaded files
        for file in uploaded_files:
            # Save the uploaded file to the 'saved_qr' directory
            path = os.path.join('saved_qr', file.name)
            with open(path, 'wb') as f:
                f.write(file.getbuffer())
            saved_paths.append(path)
        
        # Local import to avoid circular import issue
        from qr_reader import read_multiple_qr_codes
        
        # Read and decode the QR codes from the uploaded files
        data = read_multiple_qr_codes(saved_paths)
        if data:
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  # Get the current timestamp
            st.markdown("### Decoded Data")  # Display the decoded data
            # Text area to display the decoded data
            decoded_text = st.text_area("Decoded Data", f"{timestamp}\n{data}", height=150)
            if st.button("📋 Copy to Clipboard"):
                pyperclip.copy(data)  # Copy the decoded data to the clipboard
                st.success("✅ Text copied to clipboard!")  # Display a success message
        else:
            st.error("❌ Unable to decode QR Code")  # Display an error message if decoding fails

# QR Code Scanning using Webcam
elif choice == "Scan QR Code":
    st.header("Scan QR Code via Webcam")  # Set the header for QR Code scanning
    st.markdown("### Use your webcam to scan QR codes in real-time.")  # Description for QR Code scanning
    start_scan = st.button("Start Scanning")  # Button to start scanning

    if start_scan:
        import cv2  # Local import to avoid circular import issue
        cap = cv2.VideoCapture(0)  # Open the webcam
        detector = cv2.QRCodeDetector()  # Initialize the QRCode detector
        
        st.write("Scanning... Hold QR Code in front of camera")  # Display a message to prompt the user
        while True:
            _, frame = cap.read()  # Read a frame from the webcam
            data, _, _ = detector.detectAndDecode(frame)  # Detect and decode the QR code
            if data:
                st.success(f"Decoded QR Code: {data}")  # Display the decoded data
                break  # Exit the loop if a QR code is decoded
        cap.release()  # Release the webcam
        cv2.destroyAllWindows()  # Close any OpenCV windows

# Footer in Sidebar
st.sidebar.markdown("---")  # Add a horizontal line in the sidebar
st.sidebar.markdown("<footer>Developed by Y. Sathya Sai</footer>", unsafe_allow_html=True)  # Add the footer in the sidebar
