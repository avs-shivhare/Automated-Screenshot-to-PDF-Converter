# Automated-Screenshot-to-PDF-Converter
Automated Screenshot to PDF Converter

Overview

The Automated Screenshot to PDF Converter is a Python-based tool designed to automate the process of taking screenshots at specified intervals and converting them into a neatly formatted PDF document. This project is ideal for creating visual documentation, tutorials, or recording UI workflows efficiently.

Features

Automated Screenshot Capture: Captures multiple screenshots based on user-defined intervals and delay settings.

PDF Generation: Combines the captured screenshots into a single PDF document with professional formatting.

Dynamic Folder Management: Automatically organizes screenshots into uniquely named folders to prevent overwriting.

Customizable Settings: Allows users to configure the initial delay, interval between screenshots, and the number of screenshots.

How It Works

The program waits for an initial delay (default: 3 seconds).

Takes screenshots at intervals specified by the user (default: every 2 seconds).

Saves the screenshots in a dynamically created folder.

Converts all captured screenshots into a PDF file, aligning them neatly on each page.

Increments a counter to ensure filenames and folder names remain unique.

Prerequisites

Ensure the following Python libraries are installed:

pyautogui: For capturing screenshots.

Pillow (PIL): For image processing.

reportlab: For generating PDF documents.

Install the required libraries using the following commands:

pip install pyautogui pillow reportlab

Usage

Clone the repository:

git clone <repository_url>
cd <repository_folder>

Run the script:

python script_name.py

Configure the following settings in the main() function if needed:

initial_delay: Time to wait before taking the first screenshot.

interval: Time gap between consecutive screenshots.

num_screenshots: Total number of screenshots to capture.

The screenshots and the generated PDF will be saved in a folder named screenshotX (where X is the current counter value).

Example Output

Folder: screenshot1

screenshot_1_1.png

screenshot_1_2.png

screenshot_1_3.png

PDF: screenshots_1.pdf

File Structure

Project_Folder/
├── script_name.py
├── counter.txt
└── screenshotX/ (created dynamically)
    ├── screenshot_X_1.png
    ├── screenshot_X_2.png
    └── screenshots_X.pdf

Notes

Ensure your screen resolution matches the resolution defined in the take_screenshot() function (default: 1920x1080).

Grant necessary permissions for screen capture, especially on macOS and Linux.

Adjust the scaling_factor in the convert_to_pdf() function if needed for better PDF formatting.

Future Enhancements

Add GUI support for easier configuration of settings.

Enable real-time preview of captured screenshots.

Implement support for multiple screen resolutions.

License

This project is licensed under the MIT License. Feel free to use and modify it.

Author

Ashish Shivhare

