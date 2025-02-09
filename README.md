# Audio & Video Transcription and Generation Project

## 📌 Project Description
This project enables users to:
- Convert audio and video files into transcribed text using OpenAI Whisper.
- Generate synthetic speech using `gTTS` (Google Text-to-Speech) with male and female voices.
- Create videos with generated audio overlaid on an image background.

## 🚀 Features
- **Automatic Speech Recognition (ASR)**: Converts spoken content from audio/video into text.
- **Text-to-Speech (TTS)**: Generates male and female voices from the text.
- **Video Generation**: Combines generated speech with an image to create a video.

---

## 📂 Folder Structure
```
project-folder/
│── data_file/                # Folder for input audio/video files
│── transcript_file/          # Folder for storing transcriptions and generated files
│── project_file.py           # Main script for processing audio/video files
│── audio.py                  # Script for generating audio from text
│── requirements.txt          # Dependencies list
│── README.md                 # Project documentation
```
## 📊 Data Sources  
This project utilizes diverse audio and video data from multiple sources:  
- **Kaggle Dataset**: Pre-existing audio datasets from Kaggle.  
- **Self-Recorded Videos**: Custom video recordings for personalized content.  
- **YouTube Videos**: Extracted audio and video for transcription and analysis.  
- **AI-Generated Videos**: Videos generated using artificial intelligence tools.  
- **Text-to-Speech (TTS) Audio**: Synthetic audio generated via TTS for experimentation.
---

## 🛠️ Installation Guide
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/AritraOfficial/Media-Transcriber.git
cd Media-Transcriber
```


### 2️⃣ **Set Up a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Install FFmpeg**
FFmpeg is required for processing audio/video. Install it from:
- **Windows**: [Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/)
- **Linux/macOS**:
  ```bash
  sudo apt install ffmpeg  # Ubuntu/Debian
  brew install ffmpeg      # macOS (Homebrew)
  ```

## Ensure FFmpeg is added to your system `PATH`:
```bash
ffmpeg -version  # Check if FFmpeg is correctly installed
```

---

## 🏃‍♂️ Usage

### **1️⃣ Generate Speech from Text (Male & Female Voice)**
Modify the script to choose between male or female voice.
```bash
python audio.py
```

### **2️⃣ Generate Video with Background Image and Voice**
```bash
python video.py
```
This will:
- Overlay generated speech onto `background.jpg`.
- Create a video file with the generated audio.

---

### **3️⃣ Run the Transcription Script**
```bash
python project_file.py
```
This will:
- Scan `data_file/` for audio/video files.
- Use OpenAI Whisper to transcribe them.
- Save transcriptions in the `transcript_file/` folder.


## 🔧 Troubleshooting
### **1️⃣ FFmpeg Not Found**
If FFmpeg is not recognized:
- Add it to your system PATH.
- Restart your terminal after installation.

### **2️⃣ Missing Dependencies**
Run:
```bash
pip install -r requirements.txt
```

## 📜 License
This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments
- OpenAI Whisper for speech recognition.
- gTTS for text-to-speech conversion.
- MoviePy for video creation.

---

## 📞 Contact
For issues or contributions, create a GitHub issue or reach out at [Gmail](mailto:aritra.work.official@gmail.com).

