# ConsoleAppProjects 🚀

A collection of **self-motivated console-based Python projects** designed to improve coding skills and programming comprehension. These projects explore different libraries, design patterns, and real-world applications while maintaining clean, readable code.

---

## 📚 Project Overview

As time progresses, this folder will grow with new projects and updates. Each project focuses on practical functionality and best practices in Python development.

### Current Projects

---

## 1. QRCodeMaker 1.0 📱

A versatile QR code generator with dual-output capabilities.

### Features

- **Terminal Display**: Generate and display QR codes directly in the terminal using ASCII art
- **Image Export**: Save QR codes as PNG images with automatic timestamping
- **Flexible Input**: Accept any text or URL and convert to QR code
- **Smart File Management**: Automatically creates `GeneratedQR/` folder for organized output
- **User-Friendly Interface**: Interactive menu-driven experience with emoji feedback

### Technologies Used

- `qrcode` - QR code generation library
- `qrcode_terminal` - Terminal-based QR code display
- `Pillow` - Image processing
- `pathlib` - Cross-platform file path handling

### Usage

```bash
python qrmaker.py
```

**Example Workflow:**

1. Enter a link or text (e.g., `https://github.com`)
2. Choose display option:
   - Option 1: Show QR code in terminal
   - Option 2: Save as PNG image
   - Option 3: Both formats
3. QR codes are automatically saved with timestamps to prevent overwrites

### Output Structure

```
QRCodeMaker 1.0/
├── qrmaker.py
└── GeneratedQR/
    ├── qr_20240813_143022.png
    ├── qr_20240813_143045.png
    └── ...
```

---

## 2. Text-to-SpeechProgram 🗣️

A multilingual text-to-speech converter with advanced audio options.

### Features

- **20+ Language Support**: Convert text to speech in English (multiple accents), Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese, Hindi, Arabic, Dutch, Polish, Turkish, Vietnamese, Indonesian, and more
- **Speech Speed Control**: Toggle between normal and slow speech for better comprehension
- **MP3 Export**: Save generated speech as MP3 files with automatic timestamping
- **Customizable Filenames**: User-defined or auto-generated filenames
- **Audio System Initialization**: Integrated pygame mixer for audio playback
- **File Information**: Display file size and save location for each export

### Technologies Used

- `gtts` (Google Text-to-Speech) - Speech synthesis
- `pygame` - Audio system management
- `pathlib` - Cross-platform file handling
- `datetime` - Timestamp management

### Usage

```bash
python tts.py
```

**Example Workflow:**

1. Select from the main menu:
   - Save Speech to File
   - Change Language
   - Toggle Speed
   - Exit
2. Enter text to convert
3. Customize filename or accept default
4. Speech is automatically saved to `GeneratedSpeech/` folder

### Language Options

```
English (US/UK/Australia/Canada) | Spanish | French | German | Italian
Portuguese | Russian | Japanese | Korean | Chinese | Hindi | Arabic
Dutch | Polish | Turkish | Vietnamese | Indonesian
```

### Output Structure

```
Text-to-SpeechProgram/
├── tts.py
└── GeneratedSpeech/
    ├── speech_20240813_143022.mp3
    ├── speech_20240813_143045.mp3
    └── ...
```

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Dependencies

For **QRCodeMaker**:

```bash
pip install qrcode[pil] qrcode-terminal
```

For **Text-to-SpeechProgram**:

```bash
pip install gtts pygame
```

### Optional - Install All Dependencies

```bash
pip install qrcode[pil] qrcode-terminal gtts pygame
```

---

## 📁 Folder Structure

```bash
ConsoleAppProjects/
├── README.md (this file)
├── QRCodeMaker 1.0/
│   ├── qrmaker.py
│   └── GeneratedQR/
├── Text-to-SpeechProgram/
│   ├── tts.py
│   └── GeneratedSpeech/
└── ... (more projects to come)
```

---

## 🎯 Learning Goals

These projects were developed to:

- ✅ Explore different Python libraries and APIs
- ✅ Practice file I/O and path management
- ✅ Develop interactive CLI applications
- ✅ Implement error handling and user validation
- ✅ Write clean, well-documented code
- ✅ Understand design patterns and best practices

---

## 🚀 Future Enhancements

- [ ] GUI interfaces using tkinter or PyQt
- [ ] Web integration for file uploads/downloads
- [ ] Batch processing capabilities
- [ ] Configuration files for settings persistence
- [ ] Advanced error logging and debugging
- [ ] Unit tests and documentation
- [ ] Additional projects in different domains

---

## 📝 Notes

- All projects generate output files in dedicated subdirectories (e.g., `GeneratedQR/`, `GeneratedSpeech/`)
- Timestamps are used to prevent file overwrites
- Error handling is implemented throughout for graceful failure recovery
- Code follows PEP 8 style guidelines for readability

---

## 🤝 Development Approach

This is a **self-motivated learning project** where each application serves as a practical exercise in:

- Real-world problem solving
- Library integration and API usage
- User experience design
- Code organization and maintenance

---

## 📞 Notes & Tips

### QRCodeMaker

- Terminal QR codes work best with monospace fonts
- Generated images are PNG format (lossless quality)
- Large texts may require higher QR code versions

### Text-to-SpeechProgram

- gTTS uses Google's free speech synthesis service
- Internet connection required for speech generation
- MP3 files vary in size based on text length
- Slow mode is useful for learning new languages

---

## 📜 License

Free to use and modify for personal learning purposes.

---

*Last Updated: August 13, 2026*
