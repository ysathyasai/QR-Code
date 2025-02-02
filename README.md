# QR Code Generator and Reader

This project is a Streamlit application designed for generating, reading, and scanning QR codes. It provides an intuitive interface for users to create custom QR codes, decode QR codes from images, and scan QR codes in real-time using a webcam. This tool is ideal for users who need to quickly and easily work with QR codes without using complex software.

## Features

1. **Generate QR Code**: Create custom QR codes with different data types and colors.
2. **Read QR Code**: Decode QR codes from uploaded images.
3. **Scan QR Code**: Scan QR codes in real-time using a webcam.

## Detailed Explanation of Functionalities

### Generate QR Code
- **Description**: Allows users to create custom QR codes with different data types and colors.
- **Usage**: Upload an image, select the desired data type and error correction level, choose the box size, border size, and colors, and click the "Generate" button to create the QR code.

### Read QR Code
- **Description**: Decodes QR codes from uploaded images.
- **Usage**: Upload an image containing a QR code, and the application will decode and display the content.

### Scan QR Code
- **Description**: Scans QR codes in real-time using the webcam.
- **Usage**: Click the "Start Scanning" button to activate the webcam and scan QR codes.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- Install required dependencies using the command below. Ensure `requirements.txt` is present in the project directory.

   ```sh
   pip install -r requirements.txt
   ```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ysathyasai/QR_Code_Generator_Reader.git
   ```
2. Navigate to the project directory in your terminal:
   ```sh
   cd QR_Code_Generator_Reader
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```sh
   streamlit run QR_Code.py
   ```

5. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the application (or any other localhost server provided in your terminal).

## Usage
1. **Generate QR Code**: Select the "Generate QR Code" option from the sidebar, fill in the required details, and click the "Generate" button.
2. **Read QR Code**: Select the "Read QR Code" option from the sidebar, upload an image containing a QR code, and view the decoded content.
3. **Scan QR Code**: Select the "Scan QR Code" option from the sidebar, click the "Start Scanning" button, and scan QR codes using your webcam.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/ysathyasai/QR-Code/blob/main/LICENSE) file for details.

## Contributions

Any improvements, corrections, contributions, or ideas are always welcome! Feel free to open an issue or submit a pull request. For any questions or inquiries, please contact [ysathyasai.dev@gmail.com](mailto:ysathyasai.dev@gmail.com).