# QR Code Generator 🔲

A simple and elegant web-based QR code generator built with Flask and Python. Generate QR codes for any URL with a beautiful, responsive user interface.

## Features

- 🎨 Modern and responsive web interface
- 📱 Mobile and desktop compatible
- ⚡ Instant QR code generation
- 💾 Automatic download of generated QR codes
- 🔄 Easy-to-use clear button for quick input reset
- 🎯 Custom QR code logo design

## Screenshots

The application features a gradient purple background with a clean white card interface, making it visually appealing and easy to use.

## Technologies Used

- **Backend**: Flask (Python web framework)
- **QR Code Generation**: qrcode library with PIL
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with gradient themes

## Installation

### Prerequisites

Make sure you have Python installed on your device. You can download it from [python.org](https://www.python.org/downloads/).

### Step-by-Step Installation Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/DrumilPatell/qr-code.git
   cd qr-code
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install flask qrcode[pil]
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Usage

1. Open the application in your web browser
2. Enter any URL in the input field (e.g., `https://example.com`)
3. Click the "Generate & Download QR Code" button
4. The QR code will be automatically downloaded to your device
5. Use the clear (✕) button to quickly remove the current URL and enter a new one

## Project Structure

```
qr-code/
│
├── app.py                 # Flask application (main server file)
├── qr_generator.py        # Command-line QR code generator
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
│
└── templates/
    └── index.html        # Web interface template
```

## File Descriptions

- **app.py**: The main Flask web server that handles routing and QR code generation
- **qr_generator.py**: A standalone Python script for generating QR codes via command line
- **templates/index.html**: The frontend HTML template with embedded CSS and JavaScript
- **requirements.txt**: Lists all Python package dependencies

## Features in Detail

### Web Interface
- Beautiful gradient background (purple theme)
- Responsive design that works on all devices
- Real-time input validation
- Smooth animations and hover effects
- Custom QR code logo in the header

### QR Code Generation
- Supports any valid URL
- High-quality PNG output
- Automatic download functionality
- Fast generation using the qrcode library

## Dependencies

```
flask
qrcode[pil]
```

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## Development

To run the application in development mode:

```bash
python app.py
```

The Flask development server will start with debug mode enabled, allowing you to see detailed error messages and automatic reloading when you make changes to the code.

## License

This project is open source and available for personal and educational use.

## Author

**Drumil Patel**
- GitHub: [@DrumilPatell](https://github.com/DrumilPatell)

## Troubleshooting

### Common Issues

**Issue**: `ModuleNotFoundError: No module named 'flask'`
- **Solution**: Install Flask using `pip install flask`

**Issue**: `ModuleNotFoundError: No module named 'qrcode'`
- **Solution**: Install qrcode using `pip install qrcode[pil]`

**Issue**: Application doesn't start
- **Solution**: Make sure you're in the correct directory and all dependencies are installed

**Issue**: Can't access the application
- **Solution**: Ensure no other application is using port 5000, or modify the port in `app.py`

## Future Enhancements

- [ ] Customizable QR code colors
- [ ] QR code history/gallery
- [ ] Batch QR code generation
- [ ] Custom size options
- [ ] Support for vCard, WiFi credentials, and other QR code types
- [ ] API endpoint for programmatic access

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

---

Made with ❤️ by Drumil Patel
