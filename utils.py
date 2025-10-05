from cryptography.fernet import Fernet
from PIL import Image
import hashlib
import base64

def generate_key(password):
    key = hashlib.sha256(password.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))

def encrypt_message(message, password):
    fernet = generate_key(password)
    return fernet.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message, password):
    try:
        fernet = generate_key(password)
        return fernet.decrypt(encrypted_message.encode()).decode()
    except Exception:
        return None

def encode_message(image_path, message, password, output_path):
    image = Image.open(image_path)
    encoded = image.copy()
    width, height = image.size
    message = encrypt_message(message, password)
    message += "#####"
    data = ''.join([format(ord(i), '08b') for i in message])

    data_index = 0
    for y in range(height):
        for x in range(width):
            if data_index < len(data):
                pixel = list(image.getpixel((x, y)))
                for n in range(3):
                    if data_index < len(data):
                        pixel[n] = pixel[n] & ~1 | int(data[data_index])
                        data_index += 1
                encoded.putpixel((x, y), tuple(pixel))
            else:
                encoded.save(output_path)
                return True
    encoded.save(output_path)
    return True

def decode_message(image_path, password):
    image = Image.open(image_path)
    binary_data = ''
    for pixel in image.getdata():
        for n in pixel[:3]:
            binary_data += str(n & 1)
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in all_bytes:
        message += chr(int(byte, 2))
        if message[-5:] == "#####":
            try:
                decrypted = decrypt_message(message[:-5], password)
                return decrypted if decrypted else "Invalid password or corrupted image"
            except:
                return "Invalid password or corrupted image"
    return "No hidden message found"
