# CropImages

CropImages is a Python application designed to crop images using a CustomTkinter-based GUI. This tool allows users to interactively select and crop areas of images and save the cropped results.

## Features

- Load images from local storage
- Interactive cropping area selection using mouse input
- Save cropped images to a specified directory

## Prerequisites

- Python 3.x
- CustomTkinter
- Pillow (Python Imaging Library fork)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Saalim-Baba/CropImages.git
    ```

2. Navigate to the project directory:
    ```bash
    cd CropImages
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main application script:
    ```bash
    python CropImages.py
    ```

2. Follow the on-screen instructions to load an image.

3. Ibput width and height

4. Save the cropped image through the provided GUI options.

## Project Structure

- `CropImages.py`: The main script that initializes the CustomTkinter GUI, loads images, and manages cropping.
- `requirements.txt`: Lists the necessary Python packages (CustomTkinter and Pillow for image handling).

### Key Functions

- `choose_file()`: Opens a file dialog to select and display an image.
- `crop_image()`: Saves the selected cropped area as a new image file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
