from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
app._static_folder = "static"

@app.route('/gifs/<path:filename>')
def send_file(filename):
    return send_from_directory('example_gifs', filename)

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run()
