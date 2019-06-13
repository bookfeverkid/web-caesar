from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="/rotate" method="post">
            <label for="rotate-by">Rotate by:</label>
            <input id="rotate-by" type="text" name="rot" value="0" />
            <textarea name="text"></textarea>
            <input type ="submit" />
        </form>
    </body>
</html>"""

markup = """
<!doctype html>
<html>
    <body>
        <h1>{0}</h1>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/rotate", methods=['POST'])
def encrypt():
    rotate_by = int(request.form['rot'])
    text = str(request.form['text'])
    encrypted = rotate_string(text, rotate_by)
    encrypted =markup.format(encrypted)
    return encrypted
app.run()