# 🔐 Secret Code Language Translator

A Python program that encodes and decodes messages using a custom secret code language with randomized character obfuscation.

## 🚀 Features

- **Encode Messages**: Transform plain text into secret code
- **Decode Messages**: Convert secret code back to readable text
- **Random Character Generation**: Uses randomized characters for enhanced security
- **Interactive Menu**: User-friendly command-line interface
- **Robust Error Handling**: Handles edge cases and invalid inputs
- **Continuous Operation**: Process multiple messages in one session

## 🔧 How It Works

### Encoding Rules
- **Words ≥ 3 characters**: 
  - Remove the first letter and append it to the end
  - Add 3 random characters at the beginning and end
- **Words < 3 characters**: Simply reverse the string

### Decoding Rules
- **Words < 3 characters**: Reverse the string
- **Words ≥ 3 characters**:
  - Remove the first 3 and last 3 characters (random padding)
  - Move the last letter to the beginning

## 📋 Requirements

- Python 3.6 or higher
- No external dependencies required (uses only built-in modules)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/secret-code-translator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd secret-code-translator
   ```

3. Run the program:
   ```bash
   python secret_code_translator.py
   ```

## 🎯 Usage

### Interactive Mode
Run the program and follow the menu prompts:

```bash
python secret_code_translator.py
```

### Example Usage

**Encoding:**
```
Original message: Hello World
Encoded message: aBcelloH xYzorldW
```

**Decoding:**
```
Encoded message: aBcelloH xYzorldW
Decoded message: Hello World
```

## 📁 Project Structure

```
secret-code-translator/
│
├── secret_code_translator.py    # Main program file
├── README.md                    # Project documentation
└── LICENSE                      # License file
```

## 🔍 Code Overview

### Main Functions

- `generate_random_chars(length=3)`: Generates random character strings
- `encode_word(word)`: Encodes a single word according to the rules
- `decode_word(word)`: Decodes a single word according to the rules
- `encode_message(message)`: Encodes an entire message
- `decode_message(message)`: Decodes an entire message
- `main()`: Interactive menu system

### Key Features

- **Modular Design**: Each function handles a specific task
- **Error Handling**: Comprehensive input validation and edge case management
- **User-Friendly Interface**: Clear menus and informative output
- **Randomization**: Each encoding session uses different random characters

## 🧪 Testing

Test the program with various inputs:

- **Short words**: "hi", "me", "go"
- **Long words**: "programming", "encryption", "algorithm"
- **Mixed messages**: "Hello world 123"
- **Edge cases**: Single characters, empty strings

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues

- Punctuation marks are treated as part of words
- Very short messages (< 6 characters total) may not decode properly
- Case sensitivity is preserved during encoding/decoding

## 🚀 Future Enhancements

- [ ] Add support for preserving punctuation separately
- [ ] Implement different encoding algorithms
- [ ] Add file input/output functionality
- [ ] Create a GUI version
- [ ] Add encryption strength options

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Inspired by classic cipher and encoding techniques
- Built with Python's random and string modules

---

⭐ **Star this repository if you found it helpful!** ⭐
