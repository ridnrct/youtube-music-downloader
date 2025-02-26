# YouTube Music Downloader

A simple Python script that downloads YouTube videos as MP3 files with embedded thumbnails and metadata using `yt_dlp` and `ffmpeg`.

---

## Features
- Downloads the best available audio from YouTube.
- Converts audio to MP3 format (192 kbps).
- Embeds thumbnail and metadata into the MP3 file.
- Supports downloading single or multiple videos at once.

---

## Required Libraries

### 1. **yt_dlp**
A powerful command-line program to download videos from YouTube and other video sites.

### 2. **ffmpeg**
A complete, cross-platform solution to record, convert and stream audio and video. Required for:
- Converting audio to MP3.
- Embedding thumbnails (converts `.webp` images to be compatible with MP3).

---

## Installation Guide

### ✅ **1. Install Python (if not installed)**
Ensure you have Python 3.7+ installed. Download it from:
- [Python.org](https://www.python.org/downloads/)

Check Python installation:
```bash
python --version
# or
python3 --version
```

### **2. Install Required Python Libraries**

Run the following command in your terminal:
```bash
pip install yt-dlp
```

---

## Installing `ffmpeg`

### **Windows**
1. Download `ffmpeg` from the [official website](https://ffmpeg.org/download.html) or use [gyan.dev builds](https://www.gyan.dev/ffmpeg/builds/).
2. Extract the downloaded zip.
3. Copy the path to the `bin` folder (e.g., `C:\ffmpeg\bin`).
4. Add this path to the **Environment Variables**:
   - Open *System Properties* > *Advanced* > *Environment Variables*.
   - Edit the **Path** variable and add the `bin` folder path.
5. Verify installation:
```bash
ffmpeg -version
```

### **macOS**
Using Homebrew:
```bash
brew install ffmpeg
```

Verify installation:
```bash
ffmpeg -version
```