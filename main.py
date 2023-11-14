from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_cipher(text, shift):
    encrypted_text = ""

    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 89)
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char

    return encrypted_text

@app.route('/')
def index():
    return render_template('encrypt.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    shift_amount = 47

    encrypted_text = caesar_cipher(user_input, shift_amount)
    result = "Encrypted Text: " + encrypted_text
    return result

if __name__ == '__main__':
    app.run(port=8000, debug=True)
