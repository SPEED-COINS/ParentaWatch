# ParentaWatch

ParentaWatch is an innovative application designed to integrate AI, Blockchain security, and NFC authentication to provide secure parental control and monitoring solutions across various platforms (Android, iOS, Web).

## Features
- **AI Model**: Utilizes advanced AI models for monitoring.
- **Blockchain Security**: Ensures secure communication and data transfer.
- **NFC Authentication**: Supports NFC-based authentication for secure access.
- **Cross-Platform**: Available on Android, iOS, and Web.

## Project Structure
```plaintext
backend/
    ai_model.py          # AI model script
    blockchain_security.py # Blockchain security implementation
    requirements.txt     # Python dependencies

frontend/
    android/             # Android application files
    ios/                 # iOS application files
    web/                 # Web frontend files

usb/                     # USB installer scripts
    autorun-mac.plist    # Auto-run script for macOS
    usb_installer.sh     # Installer script for USB setup
