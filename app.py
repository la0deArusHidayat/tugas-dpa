from flask import Flask

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Mendefinisikan rute (route) dan fungsi view
@app.route('/')
def hello():
    return "Hello, World!"

# Menjalankan aplikasi Flask
if __name__ == '__main__':
    app.run()
