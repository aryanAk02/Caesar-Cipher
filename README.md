# Caesar Cipher 🔐

A simple Python implementation of the classic **Caesar Cipher** encryption technique. This project allows users to encrypt and decrypt messages by shifting letters of the alphabet by a specified number of positions.

## 📌 Features

- Encrypt plain text messages
- Decrypt encrypted messages
- User-friendly command-line interface
- Supports both uppercase and lowercase letters
- Handles shift values greater than 26

## 🛠️ Technologies Used

- Python 3

## 🚀 How It Works

The Caesar Cipher is a substitution cipher where each letter in the message is shifted by a fixed number of positions in the alphabet.

### Example

- Original Message: `hello`
- Shift Value: `3`
- Encrypted Message: `khoor`

Similarly, decrypting `khoor` with a shift of `3` gives back `hello`.

## ▶️ How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/aryanAk02/Caesar-Cipher.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Caesar-Cipher
   ```

3. Run the Python program:

   ```bash
   python main.py
   ```

   > Replace `main.py` with your actual Python filename if it is different.

## 📂 Project Structure

```text
Caesar-Cipher/
├── main.py
├── README.md
└── (other supporting files)
```

## 📖 Usage

1. Choose whether to encrypt or decrypt a message.
2. Enter the message.
3. Enter the shift value.
4. View the resulting output.

## Example

```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode

Type your message:
hello world

Type the shift number:
5

The encoded text is:
mjqqt btwqi
```

## 🧠 What I Learned

Through this project, I gained hands-on experience with:

- Python loops and conditional statements
- String manipulation
- Lists and indexing
- Functions and code organization
- Building interactive command-line applications

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository and submit a pull request.

## 📄 License

This project is created for educational and learning purposes.
