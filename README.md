# YouTube Video Downloader

This is a simple YouTube video downloader written in Python using the PyTube library. The script downloads the highest resolution MP4 video from a given YouTube URL.

## Features

- Downloads YouTube videos in the highest available resolution.
- Supports MP4 format.
- Simple and easy to use.

## Requirements

- Python 3.x
- pytube library

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/youtube-video-downloader.git
cd youtube-video-downloader
```

2. Install the required libraries:

```bash
pip install pytube
```

## Usage

1. Open the `downloader.py` file and update the `url` variable with the YouTube video URL you want to download:

```python
url = "https://www.youtube.com/watch?v=ZTrrc6Ni5eM"
```

2. Run the script:

```bash
python downloader.py
```

The video will be downloaded in MP4 format to the current directory.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Submit a pull request.


---

Feel free to customize this README file as needed. If you have any additional features or instructions, you can add them to the respective sections.
