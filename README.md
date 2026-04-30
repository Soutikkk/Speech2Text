# Speech-to-Text Utility

A simple, beginner-friendly Python script that captures audio from a microphone and converts it into text using the `SpeechRecognition` library and Google's Web Speech API.

## Features
- **Real-time Voice Capture**: Uses the computer's microphone to listen to your voice.
- **Ambient Noise Adjustment**: Automatically calibrates to background noise before listening.
- **Robust Error Handling**: Gracefully handles scenarios like:
  - No speech detected (timeouts)
  - Unintelligible audio
  - Network connectivity issues
  - Missing microphone or dependencies

## Prerequisites
- Python 3.x installed on your system.
- An active internet connection (required for Google's Web Speech API).
- A working microphone.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Soutikkk/Speech2Text.git
   cd Speech2Text
   ```

2. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   *Note: `PyAudio` is required to access the microphone. If you encounter installation issues with `PyAudio` on Windows, you may need to install the appropriate wheel file manually or use `pipwin install pyaudio`.*

## Usage

Run the script from your terminal:

```bash
python speech_to_text.py
```

1. Wait for the script to display: `Adjusting for ambient noise... Please wait.`
2. When it says `Listening... Speak now!`, start speaking into your microphone.
3. Wait a moment for processing. The recognized text will be printed on the screen.

## Technologies Used
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Library for performing speech recognition, with support for several engines and APIs, online and offline.
- [PyAudio](https://pypi.org/project/PyAudio/): Cross-platform audio I/O library with bindings for PortAudio.
