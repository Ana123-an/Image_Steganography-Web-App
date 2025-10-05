# 🔒 Image Steganography Web App

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-success)

> A secure and user-friendly web application that allows users to *hide* and *extract* secret messages inside images using *steganography* and *encryption*.

---

## 🚀 *Overview*

The *Image Steganography Tool* is a full-stack web app built with *Python (Flask)* and *Pillow* that lets users hide confidential messages in images with password protection. It combines *image pixel manipulation (LSB)* and *Fernet encryption* for enhanced data security.

---

## ✨ *Features*

### 🔐 Encoding
- Upload an image (PNG/JPG)
- Enter a secret message and password
- Hide the message within the image pixels
- Download the newly encoded image

### 🔍 Decoding
- Upload the encoded image
- Enter the correct password
- Retrieve and decrypt the hidden message

### 🧠 Security Highlights
- Password-protected encryption (Fernet + SHA-256)
- Messages can’t be extracted without the right password
- Temporary file cleanup for safety
- 16MB upload limit

---

## 🧩 *Tech Stack*

| Layer | Technology |
|-------|-------------|
| *Frontend* | HTML, CSS (Bootstrap-inspired) |
| *Backend* | Flask (Python) |
| *Encryption* | Cryptography (Fernet) |
| *Image Processing* | Pillow (PIL) |
| *Deployment Ready* | Works locally or on any Flask-compatible host |

---

## 🖼 *App Preview*

| Encode Message | Decode Message |
|----------------|----------------|
| ![Encode Page Screenshot](static/screenshots/encode.png) | ![Decode Page Screenshot](static/screenshots/decode.png) |

*(Add screenshots to /static/screenshots/ and update paths above.)*

---

## ⚙ *Installation & Setup*

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/image-steganography-app.git
cd image-steganography-app
