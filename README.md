# 🎬 RetroTv Converter

> ⚡ A futuristic terminal-based video converter powered by FFmpeg ⚡

RetroTv Converter is a stylish, interactive command-line tool designed to batch convert videos into TV-compatible formats — all inside a sleek, cyberpunk-inspired terminal interface.

---

## 🚀 Features

* 🎨 **Futuristic terminal UI** (powered by `rich`)
* 📂 **Interactive directory navigation**
* ⚡ **Parallel video conversion**
* 🎞️ Supports multiple formats:

  * `.mp4`, `.mkv`, `.avi`, `.mov`, `.flv`
* 🧠 Smart defaults for performance (multi-threaded conversion)
* 🖥️ Starts automatically in your **home directory**

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/supreemekoda/RetroTv.git
cd RetroTv
```

### 2. Install dependencies

```bash
pip install rich tqdm
```

### 3. Install FFmpeg

Make sure FFmpeg is installed and available in your system PATH.

* Windows: https://ffmpeg.org/download.html
* Linux:

```bash
sudo apt install ffmpeg
```

* macOS:

```bash
brew install ffmpeg
```

---

## ▶️ Usage

Run the app:

```bash
python main.py
```

---

## 🧭 Terminal Commands

Once launched, you'll enter an interactive terminal interface.

### 📍 Starting Point

* The app starts in your **home directory** (`Path.home()`)

---

### 💻 Available Commands

| Command       | Description                     |
| ------------- | ------------------------------- |
| `cd <folder>` | Enter a folder                  |
| `back`        | Go up one directory             |
| `list`        | Show files in current directory |
| `convert`     | Convert all supported videos    |
| `exit`        | Quit the app                    |

---

### 🧪 Example Workflow

```bash
>>> list
>>> cd Videos
>>> list
>>> convert
```

✔ All converted videos will be saved in:

```
converted_for_tv/
```

---

## ⚙️ Conversion Settings

Videos are converted using:

* Codec: `libx264`
* Resolution: max 1280px width
* Audio: AAC stereo
* Format: `.mp4`
* Optimized for **TV compatibility**

---

## 📁 Project Structure

```
retro_tv/
│── main.py              # Terminal UI entry point
│── batch_processor.py  # Handles batch conversion
│── converter.py        # FFmpeg logic
│── config.py           # Settings and constants
```

---

## 🎨 UI Preview

```
╔══════════════════════════════╗
║     RetroTv Converter        ║
║   ⚡ Futuristic Video Tool ⚡  ║
╚══════════════════════════════╝
```

---

## 🔥 Future Improvements

* 🎮 Full-screen terminal UI
* 🔍 Auto-complete navigation
* 📊 Live conversion stats
* 🎞️ FFmpeg output display
* 🌌 Animated interface

---

## 🤝 Contributing

Pull requests are welcome!
If you have ideas to improve the UI or performance, feel free to fork and contribute.

---

## 📜 License

MIT License

---

## ⚡ Author

Built with style and speed ⚡
