# youtube simple video and audio downloader

## Description
This project is a YouTube video and audio downloader written in Python. It uses PyInstaller to package the Python script into an executable `.exe` file so users can download videos without installing Python.

## Features
- Download YouTube videos in multiple formats.
- Extract audio from YouTube videos as `.mp3`.
- Easy-to-use and lightweight application.

## How to Use
1. **Download the executable**:
   - Go to the [Releases page](https://github.com/FadiBrahem/my-project/releases) and download the latest version of the `.exe` file.
   
2. **Run the application**:
   - Once downloaded, double-click on the `.exe` file to open the application.

3. **Enter the YouTube URL**:
   - Enter the YouTube video URL and choose whether you want to download the video or just the audio.

## Download
You can download the latest version of the executable here:  
[Download the .exe file](https://github.com/FadiBrahem/my-project/releases/download/v1.0/my-app.exe)

## Requirements (for developers)
To build the project from source or modify the code:
- Python 3.x
- Required Python libraries (see `requirements.txt`):
  ```bash
  pip install -r requirements.txt

Build the .exe (Optional)

If you want to generate the .exe yourself:

    Install PyInstaller:

    bash

pip install pyinstaller

Package the Python script:

bash

    pyinstaller --onefile main.py

License

This project is licensed under the MIT License - see the LICENSE file for details.
Contributing

Contributions are welcome! Feel free to fork this project, create a pull request, or open an issue if you find bugs or have suggestions.