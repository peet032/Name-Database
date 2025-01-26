from flask import Flask, render_template
import os

app = Flask(__name__)

def load_names(filename):
    """Load names from a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

@app.route('/')
def home():
    names = load_names('names.txt')  # Load names from the file
    return render_template('index.html', names=names)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)