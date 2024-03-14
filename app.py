from flask import Flask, send_from_directory

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('templates', 'index.html')

# Route to serve the static files (CSS, images, etc.)
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
