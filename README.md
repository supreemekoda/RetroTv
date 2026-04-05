# 📺 RetroTv

![Python](https://img.shields.io/badge/Python-3.x-blue)
![FFmpeg](https://img.shields.io/badge/FFmpeg-required-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

**RetroTv** is a lightweight Python script that converts modern video formats into **MP4 files compatible with older TVs and DVD players**.

The main script:
👉 `RetoTv.py`

---

## 🎬 Supported Formats

RetroTv can convert the following formats:

* `.mp4`
* `.mkv`
* `.avi`
* `.mov`
* `.flv`

---

## 🎯 Why RetroTv?

Many legacy devices struggle with:

* New video codecs
* High resolutions (1080p/4K)
* High bitrates

RetroTv solves this by converting videos into a **device-friendly MP4 format (H.264 + AAC)** that works on:

* 📺 Older televisions
* 💿 DVD players (USB supported)
* 📼 Legacy media players

---

## 🚀 Features

* ✅ Converts multiple video formats
* ✅ Optimized for legacy playback
* ✅ Simple command-line interface
* ✅ Fast and efficient (powered by FFmpeg)
* ✅ Batch conversion support *(if implemented)*

---

## ⚙️ Requirements

Make sure you have the following installed:

* **Python 3.x**
* **FFmpeg**

### Install FFmpeg

**Linux:**

```bash
sudo apt install ffmpeg
```

**macOS:**

```bash
brew install ffmpeg
```

**Windows:**
Download from: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
Then add FFmpeg to your system PATH.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/RetroTv.git
cd RetroTv
```

---

## ▶️ Usage

Convert a single video:

```bash
python RetoTv.py input_video.mkv
```

Convert multiple files (if supported):

```bash
python RetoTv.py *.avi
```

---

## 📁 Output

* Output files are saved as `.mp4`
* Optimized for compatibility with older devices

---

## 🔧 Encoding Details

RetroTv uses FFmpeg with settings similar to:

* **Video Codec:** H.264
* **Audio Codec:** AAC
* **Resolution:** Scaled down if needed
* **Bitrate:** Adjusted for legacy devices

---

## 🛠️ Customization

You can edit `RetoTv.py` to:

* Change resolution
* Adjust bitrate
* Force aspect ratio
* Tune output for specific devices (PAL/NTSC)

---

## ⚠️ Notes

* Original files are not modified
* Output quality depends on source file
* Very old devices may have strict limitations (e.g., resolution or bitrate caps)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Feel free to fork the project, open issues, or submit pull requests!

---
